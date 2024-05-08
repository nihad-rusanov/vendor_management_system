# Vendor Management System

## Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/nihad-rusanov/vendor_management_system.git
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

## Contributing
Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: git checkout -b feature-name.
3. Make your changes and commit them: git commit -m 'Description of your changes'.
4. Push your changes to your fork: git push origin feature-name.
5. Submit a pull request to the main repository.


## Acknowledgments
This project was inspired by the need for efficient vendor management solutions in businesses.
Special thanks to all contributors who have helped improve and maintain the project.

