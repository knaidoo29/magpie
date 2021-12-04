include "pixel_utils.f90"


subroutine which_pix_id_polar_ea_scalar(r, phi, dr, base_nphi, pix_id)

  ! Calculates the pixel index on polar equal area grid of a point in polar
  ! coordinates.
  !
  ! Parameters
  ! ----------
  ! r : float
  !   Radial coordinate.
  ! phi : float
  !   Angular coordinate.
  ! dr : float
  !   Length of radial bins.
  ! base_nphi : int
  !   Base phi grid length.
  !
  ! Returns
  ! -------
  ! pix_id : int
  !   Equal area pixel index.

  implicit none

  ! Parameter declarations

  integer, parameter :: dp = kind(1.d0)

  real(kind=dp), intent(in) :: r, phi, dr
  integer, intent(in) :: base_nphi
  integer, intent(out) :: pix_id

  real(kind=dp) :: pi, dphi, rmin, pmin
  integer :: rpix_id, phipix_id

  ! Main

  rmin = 0.
  pmin = 0.

  call which_pix_id_scalar(r, rmin, dr, rpix_id)

  pi = 4*atan(1.d0)
  dphi = 2*pi/(base_nphi*(2*rpix_id+1))

  call which_pix_id_scalar(phi, pmin, dphi, phipix_id)

  pix_id = base_nphi*rpix_id**2 + phipix_id

end subroutine which_pix_id_polar_ea_scalar


subroutine which_pix_id_polar_ea_array(r, phi, dr, base_nphi, rlen, pix_id)

  ! Calculates the pixel indices on a polar equal area grid of points in polar
  ! coordinates.
  !
  ! Parameters
  ! ----------
  ! r : array(float)
  !   Radial coordinate.
  ! phi : array(float)
  !   Angular coordinate.
  ! dr : float
  !   Length of radial bins.
  ! base_nphi : int
  !   Base phi grid length.
  !
  ! Returns
  ! -------
  ! pix_id : array(int)
  !   Equal area pixel index.

  implicit none

  ! Parameter declarations

  integer, parameter :: dp = kind(1.d0)

  integer, intent(in) :: rlen
  real(kind=dp), intent(in) :: r(rlen), phi(rlen), dr
  integer, intent(in) :: base_nphi
  integer, intent(out) :: pix_id(rlen)

  integer :: i

  ! Main

  do i = 1, rlen

    call which_pix_id_polar_ea_scalar(r(i), phi(i), dr, base_nphi, pix_id(i))

  end do

end subroutine which_pix_id_polar_ea_array
