-- Run in the test schema after restore.
SELECT COUNT(*) AS restored_row_count FROM rman_practical_sample;
SELECT sample_id, item_name, quantity FROM rman_practical_sample ORDER BY sample_id;
-- Expected sample row count before any additional inserts: 3.
