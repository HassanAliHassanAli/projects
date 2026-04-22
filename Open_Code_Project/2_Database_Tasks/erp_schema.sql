-- Create the Warehouses table to store warehouse information
CREATE TABLE Warehouses (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255)
);

-- Create the Inventory_Lots table to track inventory lots
CREATE TABLE Inventory_Lots (
  id SERIAL PRIMARY KEY,
  lot_number VARCHAR(255) NOT NULL,
  quantity INTEGER NOT NULL CHECK (quantity > 0),
  warehouse_id INTEGER REFERENCES Warehouses(id),
  FOREIGN KEY (warehouse_id) REFERENCES Warehouses(id)
);

-- Create the Suppliers table to store supplier information
CREATE TABLE Suppliers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255)
);

-- Create the Purchase_Orders table to track purchase orders
CREATE TABLE Purchase_Orders (
  id SERIAL PRIMARY KEY,
  order_date DATE NOT NULL,
  supplier_id INTEGER REFERENCES Suppliers(id),
  FOREIGN KEY (supplier_id) REFERENCES Suppliers(id)
);

-- Create the Transactions table to track transactions
CREATE TABLE Transactions (
  id SERIAL PRIMARY KEY,
  transaction_date DATE NOT NULL,
  purchase_order_id INTEGER REFERENCES Purchase_Orders(id),
  inventory_lot_id INTEGER REFERENCES Inventory_Lots(id),
  quantity_transferred INTEGER NOT NULL CHECK (quantity_transferred > 0),
  FOREIGN KEY (purchase_order_id) REFERENCES Purchase_Orders(id),
  FOREIGN KEY (inventory_lot_id) REFERENCES Inventory_Lots(id)
);

-- Create the update_stock_trigger trigger
CREATE OR REPLACE FUNCTION update_stock_trigger()
RETURNS TRIGGER AS $$
BEGIN
  UPDATE Inventory_Lots SET quantity = COALESCE(quantity - NEW.quantity_transferred, 0) WHERE id = NEW.inventory_lot_id;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_stock_trigger
BEFORE INSERT ON Transactions
FOR EACH ROW
EXECUTE FUNCTION update_stock_trigger();