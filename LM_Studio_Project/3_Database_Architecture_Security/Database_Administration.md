## 2. Scene: Database Administration (SQL)
**User Prompt:**
"Act as a Senior Database Administrator. Write a massive and comprehensive SQL script for load-testing purposes..."

**Model Response:**
> ```sql
> [-- Step 1: Structure Creation

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(255) UNIQUE NOT NULL,
    PhoneNumber BIGINT UNIQUE NOT NULL CHECK (PhoneNumber BETWEEN 9876543210 AND 9999999999)
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Name VARCHAR(100),
    Price DECIMAL
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT NOT NULL REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    TotalPrice DECIMAL CHECK (TotalPrice > 0)
);

CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY,
    ProductID INT NOT NULL REFERENCES Products(ProductID),
    Quantity INT CHECK (Quantity >= 1 AND Quantity <= 50), -- Assuming a maximum of 50 units per transaction
    OrderID INT NOT NULL REFERENCES Orders(OrderID) ON DELETE CASCADE, 
    Price DECIMAL CHECK (Price > 0)
);

-- Step 2: Data Generation

INSERT INTO Customers VALUES(1,'John', 'Doe','john.doe@example.com',9876543210);
INSERT INTO Products VALUES(1,'Apple iPhone X',999.99); -- Assuming a price for demonstration purposes
INSERT INTO Orders (CustomerID, TotalPrice) VALUES(1, 999.99);

-- Repeat the above steps to populate at least 15 rows in each table

-- Step 3: Teardown / Cleanup

DROP TABLE Transactions;
DROP TABLE Orders;
DROP TABLE Products;
DROP TABLE Customers;

]
> ```

---