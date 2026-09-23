# SOP-018 — Clinical Data Transfers

1. PURPOSE
This SOP describes the process for managing the secure transfer, validation, and handling of clinical
data between Netramind and external parties in support of clinical trials.
2. SCOPE
This procedure applies to clinical data transfers between Netramind and external parties, including
data received from clinical sites, imaging centers, and sponsors, as well as data provided by
Netramind (e.g., image-derived outputs, grading results, and datasets).
3. REFERENCES
• ICH E6(R3): Guidelines for Good Clinical Practice (GCP)
• 21 CFR Part 11 Electronic Records and Electronic Signatures
4. DEFINITIONS
4.1. Audit Trails – Metadata records that allow the appropriate evaluation of the course of events
by capturing details on actions (manual or automated) performed relating to information and
data collection and, where applicable, to activities in computerized systems. The audit trail
should show activities, initial entry, and changes to data fields or records, by whom, when and,
where applicable, why. In computerized systems, the audit trail should be secure, computer-
generated, and time stamped.
4.2. Clinical Data Transfer—A transfer of data which will be used for clinical trial operations,
analysis, or potential regulatory submission. Data transfers can be cumulative (all data) or
interim (new data or targeted data), according to the data specification plan. Examples of data
transfers include:
• Routine Data Transfer—A transfer of data which will be used for the purposes of data
review, reconciliation, and other ongoing, iterative data quality activities.
• Final Data Transfer—A transfer clinical study data which have been cleaned for database
lock or data for an interim lock.
4.3. Contract Service Provider (CSP)— A person or organization (commercial, academic or other)
providing a service used during the conduct of a clinical trial to either the sponsor or the
investigator to fulfil one or more of their trial-related activities.
4.4. Data Acquisition Tool (DAT) – Paper or electronic tool designed to collect data and associated
metadata from a data originator according to the protocol and to report the data to the
sponsor. Data originator may be a person (e.g., participant or trial staff), a device (e.g.,
wearables and sensors) or an electronic transfer of data from one system to another (e.g.,
extraction of data from an electronic health record or laboratory system). Examples of DAT
include but are not limited to case report forms (CRFs), interactive response technologies
(IRTs), patient-reported outcomes (PROs), clinical outcome assessments (COAs) and wearable
devices, irrespective of the media used.
4.5. Data Transfer Specification (DST) Plan or Agreement —A document agreed to by both
Netramind and the data service provider that describes the content and format of the data to
be transferred as well as the method of transfer. Data Transfer Specifications are known by
other names including Data Transfer Agreements and Data Transfer Plans.
5. ROLES AND RESPONSIBILITIES
5.1. Data Management
5.1.1. Work with the CSP to finalize and approve Data Transfer Specifications (DTS) for clinical
data within scope of this SOP.
5.1.2. Test data transfers and documenting the outcome.
5.1.3. Perform validation checks on data transfers to ensure adherence with DTS.
5.1.4. Review data transfers to ensure adherence to DTS complete and accurate data has been
transferred. Releasing the data for use.
5.1.5. Provide transferred files to Statistical Programming when the transfer is not automated.
5.1.6. Perform periodic reviews of audit trails and relevant metadata as part of data integrity
checks.
5.2. Statistical Programming
5.2.1. Review Data Transfer Specifications to ensure appropriate analysis and reporting
requirements are included.
5.2.2. Perform validation checks on data transfers to ensure adherence to DTS.
5.3. Biostatistics
5.3.1. Review Data Transfer Specifications to ensure appropriate analysis and reporting
requirements are included.
5.3.2. Review final and critical data transfers for adherence to DTS.
5.3.3. Accept final data transfers for analysis purposes.
6. PROCEDURE
6.1. Creating Data Transfer Specifications
6.1.1. A Data Transfer Specification (DTS) Plan should be created where structured or
recurring data transfers are expected.
6.1.2. For Netramind, data may include ophthalmic images, derived measurements, grading
outputs, adjudication decisions, and associated metadata.
6.1.3. Data Management or Statistical Programming initiates a data transfer specification with
CSP, typically using the provider’s template.
6.1.4. The Data Manager ensures the template includes:
• Relevant data acquisition tool (DAT) and systems data is collected and processed
• Source records
• Validation requirement and status
• Variable specifications
• Protection of data that can unblind (if any)
• Secure, access-controlled transfer methods (e.g., sFTP, secure cloud storage with
controlled access)
• Transfer format per agreement with Statistical Programming and Biostatistics
• Frequency, scheduled interims and types of transfer during the data lifecycle of
the clinical trial.
• Expectation for quality control of data transfers performed by CSP and/or
Sponsor.
6.1.5. The Data Manager coordinates review of the DTS Plan with relevant stakeholders (e.g.,
Biostatistics, Statistical Programming). Final approval is documented once all comments
are resolved.
6.1.6. The Data Manager manages change control throughout the data lifecycle should
changes to data structure/specifications or other transfer requirements by ensuring
that the DTS Plan is revised, reviewed, and approved according to this SOP.
6.2. Verifying Test Data Transfers
6.2.1. For data from the EDC study database
6.2.1.1.Data Managers test data extraction during user acceptance testing (UAT) of the
database if the EDC provides that capability. Otherwise, the database
specifications document, which is tested in UAT against the entry screens,
provides adequate assurance of the upcoming extracts, with the EDC and its
specifications upload process being validated software.
6.2.2. For other types of data (non-EDC)
6.2.2.1.The Data Manager oversees an initial test transfer from the CSP before the data
collection process begins and confirms that all key elements of the specification
including file names, file format, variables, and blinding are correct according to
the DTA.
6.2.2.2.The Data Manager signs the document to confirm that a test transfer was
performed and was successful.
6.2.3. If the DST plan or agreement is updated to reflect changes in the data transferred or file
contents and structure, the Data Manager must conduct and document a new test of
the transfer. Administrative changes such as updates to contact information do not
require a retest.
6.2.4. Test transfers should confirm file structure, completeness, and compatibility with
downstream systems.
6.3. Managing Data Transfers
6.3.1. The Data Manager receives the data transfer(s) via a secure transfer method and
upload the files on the Netramind dedicated and secure server if an automated transfer
via secure method is not available.
6.3.2. For routine data transfers, a Data Manager or Statistical Programmer initiates checking
of the transfer, which includes confirming that the number of files and variables are
consistent with previous transfers and that the number of data records is the same or
increasing for each file. Routine transfers should be logged or traceable, even if detailed
review is not required.
6.3.3. For critical or final transfers, validation checks should confirm data completeness,
consistency, and expected changes relative to prior transfers.
6.3.3.1.The Data Manager reviews the comparison output and researches any
differences shown. This can be verified by reviewing the metadata and/or
audit trails generated when changes are made in a system. The changes must
be valid and acceptable according with study plans and decisions.
6.3.3.2.If all differences are found to be valid, the Data Manager signs the comparison
output to indicate that the data is complete and accurate. The Data Manager
files the signed output document in the TMF.
6.3.3.3.If issues are detected, the Data Manager requests a new transfer from the CSP
and works with the CSP until all issues are resolved.
6.3.3.4.The Data Manager notifies the study team when the data is considered
available for use.
6.3.3.5.The Biostatistician confirms that the transferred data satisfy the quality
required for analysis, and which data is required for review and retention.
6.3.4. For data provided by Netramind to external parties, verification must be performed to
ensure completeness, accuracy, and alignment with agreed specifications prior to
release.
6.4. Filing and Archival of Data Transfers
6.4.1. All documentation related to data transfers, including the actual records, data transfer
files must be filed and maintained in accordance with SOP-ABC-123 GxP Record
Management procedures.
7. ATTACHMENTS
• Appendix I: Workflow for Data Transfers
8. REVISION HISTORY
Date Summary of Change(s)
VERSION
NUMBER
01 01-MAY-2026 New Document
[X.0] [DD-MMM-YYYY] [Insert a summary of the changes]
SIGNATURE PAGE
AUTHOR
NAME TITLE SIGNATURE DATE
JUSTIN SHAKA FRACTIONAL COO 01-MAY-2026
REVIEWER
NAME TITLE SIGNATURE DATE
APPROVER
NAME TITLE SIGNATURE DATE
Appendix I: Workflow for Data Transfers
