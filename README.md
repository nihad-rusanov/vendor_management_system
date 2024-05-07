# Vendor Management System

## Setup Instructions

1. Clone the repository:
   git clone https://github.com/your-username/vendor-management-system.git
   cd vendor-management-system
   
2. Install dependencies:
   pip install -r requirements.txt

3. Apply migrations:
   python manage.py migrate

4. Create a superuser account:
   python manage.py createsuperuser

5. Run the development server:
   python manage.py runserver

1. Clone the repository
```bash
git clone https://github.com/your-username/vendor-management-system.git
cd vendor-management-system
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Apply migrations
```bash
python manage.py migrate
```
4. Create a superuser account
```bash
python manage.py createsuperuser
```
5. Run the development server
```bash
python manage.py runserver
```


## API Endpoints

### Vendor Profile Management
  - **POST** `/api/vendors/`: Create a new vendor.
  - **GET** `/api/vendors/`: List all vendors.
  - **GET** `/api/vendors/{vendor_id}/`: Retrieve a specific vendor's details.
  - **PUT** `/api/vendors/{vendor_id}/`: Update a vendor's details.
  - **DELETE** `/api/vendors/{vendor_id}/`: Delete a vendor.
  
### Purchase Order Tracking
  - **POST** `/api/purchase_orders/`: Create a purchase order.
  - **GET** `/api/purchase_orders/`: List all purchase orders with an option to filter by vendor.
  - **GET**  `/api/purchase_orders/{po_id}/`: Retrieve details of a specific purchase order.
  - **PUT** `/api/purchase_orders/{po_id}/`: Update a purchase order.
  - **DELETE** `/api/purchase_orders/{po_id}/`: Delete a purchase order.
  
### Vendor Performance Evaluation
  - **GET** `/api/vendors/{vendor_id}/performance/`: Retrieve a vendor's performance metrics.
  Authentication
  Token-based authentication is required to access protected endpoints.
  Obtain a token by sending a **POST** request to `/api/token/`.
  Include the token in the Authorization header of subsequent requests: Authorization: Bearer <token>.

