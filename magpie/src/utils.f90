
subroutine linspace(xmin, xmax, n, x)
  ! Outputs n linearly spaced points between xmin and xmax.
  !
  ! Parameters
  ! ---------
  ! xmin : float
  !   Minimum x value.
  ! xmax : float
  !   Maximum x value.
  ! n : int
  !   Number of points.
  !
  ! Returns
  ! -------
  ! x : array
  !   Linearly space points.

  implicit none

  integer, parameter :: dp = kind(1.d0)

  integer, intent(in) :: n
  real(kind=dp), intent(in) :: xmin, xmax
  real(kind=dp), intent(out) :: x(n)

  integer :: i
  real(kind=dp) :: dx

  dx = (xmax-xmin)/(n-1)

  x(1) = xmin

  do i = 2, n
    x(i) = xmin + (i-1)*dx
  end do

end subroutine linspace

subroutine midpoint(x, n, xmid)
  ! Outputs the midpoints of array x
  !
  ! Parameters
  ! ---------
  ! x : array
  !   array values.
  ! n : int
  !   Number of points in x.
  !
  ! Returns
  ! -------
  ! xmid : array
  !   Midpoint of two adjacent points in x.

  implicit none

  integer, parameter :: dp = kind(1.d0)

  integer, intent(in) :: n
  real(kind=dp), intent(in) :: x(n)
  real(kind=dp), intent(out) :: xmid(n-1)

  integer :: i

  do i = 1, n-1
    xmid(i) = 0.5*(x(i) + x(i+1))
  end do

end subroutine midpoint
