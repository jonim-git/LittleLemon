# LittleLemon

Usage:

Registration

Make a user in 
http://127.0.0.1:8000/admin/

Make a post request with the user information you just made
http://127.0.0.1:8000/restaurant/api-token-auth/

Example:

{
	"username":"testuser",
	"password":"password123!"
}

Use the token from the response to retrieve items from bookings endpoint

menu items:
get/post
http://127.0.0.1:8000/restaurant/menu/2

single menu item:
get/ put/ delete
http://127.0.0.1:8000/restaurant/menu/1

Bookings:

All bookings
get/post
http://127.0.0.1:8000/restaurant/booking/tables/

Single booking
get/put/delete
http://127.0.0.1:8000/restaurant/booking/tables/2/



