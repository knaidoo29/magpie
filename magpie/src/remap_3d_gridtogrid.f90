include "utils.f90"

subroutine remap_3d_gridtogrid(d1, x, y, z, boxsize, grid1, grid2, sperpix, d2)
  ! Resamples a dataset defined on 2D cartesian grid onto a new 2D cartesian grid.
  !
  ! Parameters
  ! ----------
  ! d1 : array
  !   The values of the 3D grid pixels.
  ! x, y : array
  !   Centers of pixels located on the output 2D grid.
  ! boxsize : float
  !   Size of the box.
  ! grid1 : int
  !   Size of the input 3D grid along one axis.
  ! grid2 : int
  !   Size of the output 3D grid along one axis.
  ! sperpix : int
  !   The number of samples evenly spaced along each axis for constructing the new 3D grid.
  !
  ! Returns
  ! -------
  ! d2 : array
  !   The resampled pixel values for the output 3D cartesian grid.

  implicit none

  integer, parameter :: dp = kind(1.d0)

  integer, intent(in) :: grid1, grid2, sperpix
  real(kind=dp), intent(in) :: d1(grid1*grid1*grid1), x(grid2*grid2*grid2), y(grid2*grid2*grid2), z(grid2*grid2*grid2), boxsize
  real(kind=dp), intent(out) :: d2(grid2*grid2*grid2)

  real(kind=dp) :: dx1, dx2, xperpix_edges(sperpix+1), xperpix(sperpix)
  real(kind=dp) :: mhdx2, phdx2
  integer :: i, ixp, iyp, izp, ixconv, iyconv, izconv, iconv

  dx1 = boxsize / FLOAT(grid1)
  dx2 = boxsize / FLOAT(grid2)

  mhdx2 = -0.5*dx2
  phdx2 = 0.5*dx2

  call linspace(mhdx2, phdx2, sperpix+1, xperpix_edges)
  call midpoint(xperpix_edges, sperpix+1, xperpix)

  do i = 1, grid2*grid2*grid2
    d2(i) = 0.

    do ixp = 1, sperpix
      do iyp = 1, sperpix
        do izp = 1, sperpix
          ixconv = INT(FLOOR((x(i) + xperpix(ixp))/dx1))
          iyconv = INT(FLOOR((y(i) + xperpix(iyp))/dx1))
          izconv = INT(FLOOR((z(i) + xperpix(izp))/dx1))
          iconv = izconv + grid1*(iyconv + grid1*ixconv) + 1
          d2(i) = d2(i) + d1(iconv)
        end do
      end do
    end do

    d2(i) = d2(i)/(FLOAT(sperpix)**3.)
  end do


end subroutine remap_3d_gridtogrid
