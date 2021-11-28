
subroutine rotate_2d_scalar(x, y, dphi, xrot, yrot)

  ! Rotates a single point in 2D cartesian coordinates counter clockwise by
  ! dphi in radians.
  !
  ! Parameters
  ! ----------
  ! x, y : float
  !   Cartesian coordinates.
  ! dphi : float
  !   Counter-clockwise rotation.
  !
  ! Returns
  ! -------
  ! xrot, yrot : float
  !   Rotated x and y coordinates.

  implicit none

  ! Parameter declarations

  integer, parameter :: dp = kind(1.d0)
  real(kind=dp), intent(in) :: x, y, dphi
  real(kind=dp), intent(out) :: xrot, yrot

  ! Main

  xrot = cos(dphi)*x - sin(dphi)*y
  yrot = sin(dphi)*x + cos(dphi)*y

end subroutine rotate_2d_scalar


subroutine rotate_2d_array(x, y, dphi, xlen, xrot, yrot)

  ! Rotates an array of points in 2D cartesian coordinates counter clockwise by
  ! dphi in radians.
  !
  ! Parameters
  ! ----------
  ! x, y : array
  !   Cartesian coordinates.
  ! dphi : float
  !   Counter-clockwise rotation.
  !
  ! Returns
  ! -------
  ! xrot, yrot : array
  !   Rotated x and y coordinates.

  implicit none

  ! Parameter declarations

  integer, parameter :: dp = kind(1.d0)
  integer, intent(in) :: xlen
  real(kind=dp), intent(in) :: x(xlen), y(xlen), dphi
  real(kind=dp), intent(out) :: xrot(xlen), yrot(xlen)

  integer :: i

  ! Main

  do i=1, xlen

    call rotate_2d_scalar(x(i), y(i), dphi, xrot(i), yrot(i))

  end do

end subroutine rotate_2d_array
