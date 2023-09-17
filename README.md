# LittleLemon

## Usage:

### Registration

1. Create a user in the [admin panel](http://127.0.0.1:8000/admin/).

2. Make a POST request with the user information you just created to obtain an authentication token.

   API Endpoint: [http://127.0.0.1:8000/restaurant/api-token-auth/](http://127.0.0.1:8000/restaurant/api-token-auth/)

   Example Request Body:
   ```json
   {
       "username": "testuser",
       "password": "password123!"
   }

Use the token from the response to access protected endpoints.

**Menu Items:**
- **Get/Post Menu Items:**
  - API Endpoint: [http://127.0.0.1:8000/restaurant/menu/2](http://127.0.0.1:8000/restaurant/menu/2)

- **Single Menu Item (Get/Put/Delete):**
  - API Endpoint: [http://127.0.0.1:8000/restaurant/menu/1](http://127.0.0.1:8000/restaurant/menu/1)

**Bookings:**
- **All Bookings (Get/Post):**
  - API Endpoint: [http://127.0.0.1:8000/restaurant/booking/tables/](http://127.0.0.1:8000/restaurant/booking/tables/)

- **Single Booking (Get/Put/Delete):**
  - API Endpoint: [http://127.0.0.1:8000/restaurant/booking/tables/2/](http://127.0.0.1:8000/restaurant/booking/tables/2/)
