include "pixel_utils.f90"


subroutine get_remap_pix_len(x1min, x1max, grid1, x2min, x2max, grid2, pixlen)
  ! Find pixel weight length.
  !
  ! Parameters
  ! ----------
  ! x1min : float
  !   Minimum in grid 1.
  ! x1max : float
  !   Maximum in grid 1.
  ! grid1 : int
  !   Number of grid points in grid 1.
  ! x2min : float
  !   Minimum in grid 2.
  ! x2max : float
  !   Maximum in grid 2.
  ! grid2 : int
  !   Number of grid points in grid 2
  !
  ! Returns
  ! -------
  ! pixlen : int
  !   Length of pixel mapping indices and weights.

  implicit none

  ! Parameter declarations

  integer, parameter :: dp = kind(1.d0)

  integer, intent(in) :: grid1, grid2
  real(kind=dp), intent(in) :: x1min, x1max, x2min, x2max

  real(kind=dp) :: boxsize1, boxsize2, dx1, dx2

  integer, intent(out) :: pixlen

  ! Main

  boxsize1 = x1max - x1min
  boxsize2 = x2max - x2min

  dx1 = boxsize1 / real(grid1)
  dx2 = boxsize2 / real(grid2)

  pixlen = int(floor(dx2/dx1)) + 2

end subroutine get_remap_pix_len


subroutine remap_1d_grid2grid_pixel(x1min, x1max, grid1, x2min, x2max, grid2 &
  , which2pix, pixlen, pix_id, weights)

  ! Computes the exact weights for mapping a single pixel from a new grid
  ! (denoted by 2) onto an initial grid (denoted with 1).
  !
  ! Parameters
  ! ----------
  ! x1min : float
  !   Minimum in grid 1.
  ! x1max : float
  !   Maximum in grid 1.
  ! grid1 : int
  !   Number of grid points in grid 1.
  ! x2min : float
  !   Minimum in grid 2.
  ! x2max : float
  !   Maximum in grid 2.
  ! grid2 : int
  !   Number of grid points in grid 2.
  ! which2pix : int
  !   Pixel in grid 2.
  ! pixlen : int
  !   Length of pixel mapping indices and weights.
  !
  ! Returns
  ! -------
  ! pix_id : int
  !   Pixels to map 2 to 1.
  ! weights : floats
  !   Weights to map 2 to 1.

  implicit none

  ! Parameter declarations

  integer, parameter :: dp = kind(1.d0)

  integer, intent(in) :: grid1, grid2, which2pix, pixlen
  real(kind=dp), intent(in) :: x1min, x1max, x2min, x2max
  integer, intent(out) :: pix_id(pixlen)
  real(kind=dp), intent(out) :: weights(pixlen)

  real(kind=dp) :: boxsize1, boxsize2, dx1, dx2
  real(kind=dp) :: x1edge1, x1edge2, x2edge1, x2edge2
  integer :: i, pix1, pix2

  ! Main

  boxsize1 = x1max - x1min
  boxsize2 = x2max - x2min

  dx1 = boxsize1 / real(grid1)
  dx2 = boxsize2 / real(grid2)

  x2edge1 = x2min + dx2*real(which2pix)
  x2edge2 = x2min + dx2*real(which2pix+1)

  call which_pix_id_scalar(x2edge1, x1min, dx1, pix1)
  call which_pix_id_scalar(x2edge2, x1min, dx1, pix2)

  if (pix1 .NE. pix2) then
    do i = 1, pixlen
      pix_id(i) = pix1 + i-1
      if ((pix_id(i) .GE. 0) .AND. (pix_id(i) .LT. grid1)) then
        x1edge1 = x1min + dx1*real(pix_id(i))
        x1edge2 = x1min + dx1*real(pix_id(i)+1)
        if ((x2edge1 .GE. x1edge1) .AND. (x2edge2 .LE. x1edge2)) then
          weights(i) = (x2edge2 - x2edge1)/(x2edge2 - x2edge1)
        else if ((x2edge1 .LT. x1edge1) .AND. (x2edge2 .LE. x1edge2) &
          .AND. (x2edge2 .GT. x1edge1)) then
          weights(i) = (x2edge2 - x1edge1)/(x2edge2 - x2edge1)
        else if ((x2edge1 .GE. x1edge1) .AND. (x2edge1 .LT. x1edge2) &
          .AND. (x2edge2 .GT. x1edge2)) then
          weights(i) = (x1edge2 - x2edge1)/(x2edge2 - x2edge1)
        else if ((x2edge1 .LT. x1edge1) .AND. (x2edge2 .GT. x1edge2)) then
          weights(i) = (x1edge2 - x1edge1)/(x2edge2 - x2edge1)
        else
          weights(i) = 0.
          pix_id(i) = -1
        end if
      else
        weights(i) = 0.
        pix_id(i) = -1
      end if

    end do
  else if (pix1 .NE. -1) then
    do i = 1, pixlen
      pix_id(i) = pix1 + i-1
      if ((pix_id(i) .GE. 0) .AND. (pix_id(i) .LT. grid1)) then
        if (i .EQ. 1) then
          weights(i) = 1.
        else
          weights(i) = 0.
        end if
      else
        weights(i) = 0.
        pix_id(i) = -1
      end if
    end do
  end if

end subroutine remap_1d_grid2grid_pixel
