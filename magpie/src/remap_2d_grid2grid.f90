include "remap_1d_grid2grid.f90"


subroutine remap_2d_grid2grid(x1min, x1max, xgrid1, y1min, y1max, ygrid1 &
  , x2min, x2max, xgrid2, y2min, y2max, ygrid2, xpixlen, ypixlen, f1, f2)

  ! Remaps field 1 onto field 2 using exact weights.
  !
  ! Parameters
  ! ----------
  ! x1min : float
  !   Minimum x in grid 1.
  ! x1max : float
  !   Maximum x in grid 1.
  ! xgrid1 : int
  !   Number of grid points in grid 1 along x.
  ! y1min : float
  !   Minimum y in grid 1.
  ! y1max : float
  !   Maximum y in grid 1.
  ! ygrid1 : int
  !   Number of grid points in grid 1 along y.
  ! x2min : float
  !   Minimum x in grid 2.
  ! x2max : float
  !   Maximum x in grid 2.
  ! xgrid2 : int
  !   Number of grid points in grid 2 along x.
  ! y2min : float
  !   Minimum y in grid 2.
  ! y2max : float
  !   Maximum y in grid 2.
  ! ygrid2 : int
  !   Number of grid points in grid 2 along y.
  ! xpixlen : int
  !   Length of pixel mapping indices and weights along x.
  ! ypixlen : int
  !   Length of pixel mapping indices and weights along y.
  ! f1 : array
  !   Values on grid 1.
  !
  ! Returns
  ! -------
  ! f2 : array
  !   Remapped field 1 onto field 2.

  implicit none

  ! Parameter declarations

  integer, parameter :: dp = kind(1.d0)

  integer, intent(in) :: xgrid1, ygrid1, xgrid2, ygrid2, xpixlen, ypixlen
  real(kind=dp), intent(in) :: x1min, x1max, x2min, x2max
  real(kind=dp), intent(in) :: y1min, y1max, y2min, y2max
  real(kind=dp), intent(in) :: f1(xgrid1*ygrid1)
  real(kind=dp), intent(out) :: f2(xgrid2*ygrid2)
  real(kind=dp) :: xweights(xpixlen), yweights(ypixlen)
  integer :: xpix(xpixlen), ypix(ypixlen), pix(xpixlen*ypixlen), i, j, xwhich2pix, ywhich2pix, ii, jj, i1, j1

  ! Function

  do i = 1, xgrid2

    xwhich2pix = i-1
    call remap_1d_grid2grid_pixel(x1min, x1max, xgrid1, x2min, x2max, xgrid2, xwhich2pix, xpixlen, xpix, xweights)

    do j = 1, ygrid2

      ywhich2pix = j-1
      call remap_1d_grid2grid_pixel(y1min, y1max, ygrid1, y2min, y2max, ygrid2, ywhich2pix, ypixlen, ypix, yweights)

      call pix1dto2d(xpix, ypix, xpixlen, ypixlen, ygrid1, pix)

      ii = ywhich2pix + ygrid2*xwhich2pix + 1
      f2(ii) = 0.

      jj = 1

      do i1 = 1, xpixlen
        do j1 = 1, ypixlen

          if (pix(jj) .NE. -1) then
            f2(ii) = f2(ii) + xweights(i1)*yweights(j1)*f1(pix(jj)+1)
          end if

          jj = jj + 1

        end do
      end do

    end do
  end do

end subroutine remap_2d_grid2grid
