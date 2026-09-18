# NM-OPS-DAT-002-v1.0 — Customer Data Backup & Retention Procedure

## 1. Purpose
To ensure customer data can be recovered after accidental loss, corruption,
or a system failure, and is retained only as long as required.

## 2. Scope
Applies to all production databases and file stores holding customer data.

## 3. Responsibilities
- On-call engineer: verifies the nightly backup job completed successfully.
- Data owner (department lead): approves any restore to production.

## 4. Procedure
1. Automated nightly backups run at 02:00 UTC for every production database.
2. Backups are encrypted at rest and stored in a separate region from the
   source system.
3. The on-call engineer checks the backup job status each morning and files
   an incident if a backup failed two nights in a row.
4. Backups are retained for 35 days on a rolling basis, then deleted.
5. A restore drill is run quarterly against a staging environment to confirm
   backups are actually recoverable.

## 5. References
- Netramind Data Retention Policy

## 6. Revision History
| Version | Date | Change |
|---|---|---|
| 1.0 | 2025-12-01 | Initial release |
