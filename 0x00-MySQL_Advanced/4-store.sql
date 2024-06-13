--  script that creates a trigger that decreases the quantity of an item after adding a new order.
CREATE TRIGGER decrease_qunatity
AFTER INSERT ON orders
FOR EACH ROW
	UPDATE items SET quantiy = quanitity - NEW.number
	WHERE name = NEW.item_name
