# Oracle RMAN Full Backup and Restore Practical

**Aim:** Perform a full backup and restore of a sample Oracle database using RMAN.

## Procedure
1. Use an isolated Oracle test instance or disposable VM only.
2. Run `create_test_data.sql` in a test schema and confirm the sample rows.
3. Confirm ARCHIVELOG mode and the backup destination with your instructor/DBA.
4. Edit the disk path in `full_backup.rman`, then run it in RMAN.
5. Verify using `LIST BACKUP SUMMARY;` and `RESTORE DATABASE VALIDATE;`.
6. For the restore exercise, use a separate disposable target and review `restore_recover.rman` with your DBA/instructor before executing.
7. Run `validate.sql` and confirm the restored sample row count.

Example: `rman target /` then `LIST BACKUP SUMMARY;`.

**Safety:** RMAN is Oracle tooling, separate from the PostgreSQL application. Restore/recovery can overwrite database files. Confirm DBID, Oracle version, paths, control-file/SPFILE handling and archive-log availability. Never run this against production. The scripts are templates, not universal commands.
