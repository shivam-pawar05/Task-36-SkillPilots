-- Run as a test schema owner in an isolated Oracle lab.
CREATE TABLE rman_practical_sample (
    sample_id NUMBER PRIMARY KEY,
    item_name VARCHAR2(100) NOT NULL,
    quantity NUMBER NOT NULL,
    created_at TIMESTAMP DEFAULT SYSTIMESTAMP
);
INSERT INTO rman_practical_sample VALUES (1, 'Keyboard', 25, SYSTIMESTAMP);
INSERT INTO rman_practical_sample VALUES (2, 'Mouse', 40, SYSTIMESTAMP);
INSERT INTO rman_practical_sample VALUES (3, 'Monitor', 10, SYSTIMESTAMP);
COMMIT;
SELECT * FROM rman_practical_sample ORDER BY sample_id;
