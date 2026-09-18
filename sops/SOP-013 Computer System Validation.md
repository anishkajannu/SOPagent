# SOP-013 — Computer System Validation

1 PURPOSE
This Standard Operating Procedure (SOP) outlines the procedure required for initial validation and
maintenance of the validated state in computerized systems used by Netramind for GxP activities.
2 SCOPE
This procedure applies to computerized systems used by Netramind in support of GxP-regulated
activities, including clinical data analysis workflows and related supporting systems where validation
is determined to be appropriate based on system risk and intended use.
3 REFERENCES
• SOP-015 21 CFR Part 11
• SOP-016 Data Integrity
• SOP-004 GxP Records Retention
• GAMP 5—A Risk-Based Approach to Compliant GxP Computerized Systems
• International Conference on Harmonization (ICH) E6 (R3) Good Clinical Practice
• International Conference on Harmonization (ICH) Q7: Good Manufacturing Practice Guide for
Active Pharmaceutical Ingredients; November 2000
• Food and Drug Administration (FDA): 21 CFR Part 11; 21 CFR parts 210 and 211 and 820
• European Medicines Agency (EMA): EudraLex Volume 4, Part 1: Basic Requirements for
Medicinal Products; Annex 11: Computerized Systems
• European Medicines Agency (EMA): Guideline on computerized systems and electronic data in
clinical trials
4 DEFINITIONS
4.1 Acceptance Criteria—The established standard that a system or component must satisfy
for a result to be acceptable to the user, customer or other authorized entity.
4.2 Change Control Request Form—An official request for prospective approval to
implement a change to a validated system.
4.3 Commercial Off-the-Shelf (COTS) System — A commercially available electronic
system (including hardware or software) that can be purchased from third-party vendors.
4.4 Computerized System—The set of hardware, software, peripheral devices, personnel, and
documentation needed to perform a specific group of functions to meet a business or
regulatory need. A Computer System (defined above) is a component of a Computerized
System.
4.5 Computerized Systems Validation (CSV)—A process of establishing and documenting that
the specified requirements of a computerized system can be consistently fulfilled from design
until decommissioning of the system or transition to a new system. The approach to
validation should be based on a risk assessment that takes into consideration the intended use
of the system and the potential of the system to affect trial participant protection and the
reliability of trial results.
4.6 Design Specifications—Document which captures the design of a system or system
component to satisfy specified requirements.
4.7 Functional Requirements Specification (FRS)— The Functional requirements contain
User Requirements and Functional Specifications. It describes the Computerized System
in terms of the functions it will perform, and facilities required to meet the User
Requirements. They also document the fundamental processes or transformations that
the Computerized System performs on inputs to produce outputs.
4.8 Process/Business Owner—The person ultimately responsible for the business process or
processes being managed. The process owner is responsible for ensuring that the
computerized system and its operation is in compliance and fit for intended use in
accordance with applicable Standard Operating Procedures (SOPs) throughout its useful
life. Responsibility for control of system access should be agreed between process and
system owner. In some cases, the process owner also may be the system owner.
4.9 Subject Matter Expert (SME)— Individuals with highest level of expertise/competency in
skills or performing specialized tasks who can provide specific detailed knowledge or
expertise.
4.10Traceability Matrix (TM)— A matrix that maps the specification requirements to the test
scripts verifying that the specification was met.
4.11User Requirements Specification (URS)—Document that describes what the equipment
or system is supposed to do and is normally written by the user. The UR includes all
essential requirements (musts), and if possible, a prioritized list of desirable requirements
(should). Requirements should be linked to the PQ, which tests the system in its operating
environment, including the associated procedures.
4.12Validation Plan (VP)—A formal document providing a framework that describes the
validation process, responsibilities, documentation deliverables, timelines, acceptance
criteria and maintenance of the validated state for a given computerized system. The VP
encompasses the system’s lifecycle (development, implementation, use and retirement).
4.13Validation Summary Report (VSR)—A document that summarizes the validation
activities, exceptional conditions occurring during testing and the justification for
releasing for use or continued use of the system.
5 RESPONSIBILITIES
5.1 Business Owner (BO) or Designee
5.1.1 Defines intended system use and business requirements.
5.1.2 Ensures systems remain appropriate for intended use.
5.2 Quality Assurance (QA) System Validation or Designee
5.2.1 Provides oversight for validation activities where applicable.
5.2.2 Ensures validation documentation and records are maintained appropriately.
5.3 Subject Matter Expert (SME) or Designee
5.3.1 Participate in requirements definition, testing, and operational evaluation activities
where applicable.
5.3.2
5.4 Technical Team / Information Technology (IT) CSV or Designee
5.4.1 Supports implementation, maintenance, and testing activities.
5.4.2 Maintains system infrastructure and technical configurations.
6 PROCEDURE
6.1 Computer System Validation Service Request
6.1.1 The Business Owner identifies the potential need for validation and identifies the
potential need for validation activities associated with a new system, system
change, or new intended use.
6.2 Computerized System Regulatory Assessment
6.2.1 Appropriate personnel perform a regulatory and risk assessment for computerized
systems where applicable.
6.2.2 Systems may be categorized based on complexity, configuration, customization,
and regulatory impact to support determination of appropriate validation activities.
6.2.2.1 The 21 CFR Part 11 Electronic Records and Electronic Signatures
Assessment—Performed to determine if 21 CFR Part 11 regulations are
applicable to the computerized system. The assessment includes
determining if the system will create, modify, maintain, archive, retrieve,
or transmit electronic records that will be used to satisfy FDA and EU
established rules and if the system is appropriate for use of electronic
signatures.
6.2.2.2 GxP Assessment—Performed to check if the computer system has a
potential to impact on the safety and efficacy of a medicinal product.
6.3 Validation Methodology
6.3.1 Netramind applies a risk-based validation approach informed by GAMP 5
principles where appropriate.
6.3.2 Validation Document Numbering—The documents generated as a part of the computer
systems lifecycle will have a unique document number in the format CSV-AAA-
XXXX.YY where:
• AAA is the abbreviation of the document (e.g., VP for Validation Plan).
• XXXX is the sequential number of each validation project.
• YY is the version number of the document.
• For example, the document number for Validation Plan for the system is CSV-VP-
0001.00.
6.4 Validation Process
6.4.1 Planning Phase
During the planning phase, the following validation activities are performed.
6.4.1.1 The Business Owner along with appropriate personnel create the Business
Requirements Specification (BRS) and the document is reviewed and
approved as appropriate.
6.4.1.2 The BRS defines the criteria by which the system will be validated against
and includes the following, as applicable:
a. User Requirements (UR): A User Requirements document will be
produced by the business owner. This document will document the
system’s business and functional requirements from a user’s
perspective. It includes statements of the features that need to be
delivered in the final solution that will satisfy the need, goals and
objectives defined in the scope. It may include business process
diagrams and flowcharts as applicable. It will also include any
applicable regulatory requirements including all GxP user
requirements. The requirements are independent of the particular
hardware and software that are chosen for a specific system.
• UR Identifier: Unique requirement number is required for each
requirement for an easy reference.
• Requirements may be prioritized based on business, regulatory, and
operational impact.
b. Functional Specification (FS): A functional Specification (FS) will be
produced by the project team if applicable. It will include a description
of the system in terms of the functions it will perform to meet the user
requirements as defined in the UR. The FS should be detailed enough to
ensure that functionality, design constraints, attributes, interfaces,
calculations are specified.
• FS Identifier: Unique requirement number is required for each
specification for an easy reference and must map to at least one user
requirement.
6.4.1.3 Contract Service Provider/Supplier Assessment and Audit: Vendor or
supplier assessments may be performed where appropriate based on
system risk and intended use.
6.4.1.4 Risk Assessment: IT QA along with SME performs a Risk Assessment for
all systems. The Business Owner reviews and approve the assessment. The
purpose of the Risk Assessment is to determine the risk associated with
implementing the proposed new computer system or update to an existing
system.
6.4.1.5 Validation Plan: Validation activities and documentation may be planned
and documented based on system risk, complexity, and intended use.
Traceability between requirements, testing activities, and implemented
functionality may be maintained where appropriate.
6.4.1.6 Where vendor/supplier is involved, a review of the vendor/supplier
documentation must be performed and documented to ensure that it is
consistent with requirements specified within applicable regulatory
agencies and Netramind procedures.
6.4.1.7 Design Specification: The Design Specification provides detailed
information about the actual system and includes the following:
• High-level system overview
• Development and Testing methodology applied
• List of hardware and software components
• Database design, including audit trails
• Report formats
• Details of interfaces with other systems and users
• Security
• Data Requirements including Data Migration if applicable
6.4.1.8 Configuration Specification: The purpose of the Configuration
Specification is to provide more detailed specifications. Configuration
details relevant to system operation, security, and intended use may be
documented where appropriate.
6.4.2 Validation Testing Phase
Validation and testing activities are performed based on system risk, intended use,
and complexity to provide reasonable assurance that systems function as
intended.
6.4.2.1 Testing activities may include installation verification, functional testing,
user acceptance testing, integration testing, or other verification activities
as appropriate.
6.4.2.2 Data Migration Plan: Where applicable, data migration activities are
planned and verified to ensure data integrity and completeness are
maintained.
6.4.3 System Release
6.4.3.1 Systems may be released for operational use following completion of
appropriate validation, testing, approval, and training activities where
applicable.
6.4.3.2 Training Materials and Training Users: Written procedures, Training
materials or work instructions will be created and approved as applicable.
Relevant users are trained on applicable systems and procedures prior to
operational use where appropriate.
6.4.3.3 Validation activities and outcomes may be summarized in validation
records or reports as appropriate based on system risk and complexity.
6.4.3.4 Update Computer System Inventory: Once the Validation Summary
Report is approved, the IT QA prepare and update the computer system
inventory that includes:
• Project name
• System name and description in short
• Version number of the system
• Risk Level / Results of assessment
• Business owner
• System location
• Status of the system
6.5 Operation and Maintenance Phase
6.5.1 Once the system has been released for use the operation and maintenance process
begins. During this period, the system is operating normally, and any deviations
that occur are documented, examined and corrected. Periodic reviews are
performed to ensure that the validated state is maintained.
6.5.1.1 Validation Periodic Review: Periodic reviews may be performed for
validated systems based on system risk, complexity, criticality, and rate of
change to confirm systems remain appropriate for intended use.
6.6 Change Control
6.6.1 Changes to validated systems are managed through the IT Change Control process.
Validation impact assessments are performed where appropriate based on the
nature and risk of the change.
6.7 Retirement Phase
6.7.1 Validated systems are to be retired when no longer in Use. This process consists of
withdrawal of the system from use and archival of data from the system.
6.7.2 Retirement activities may include decommissioning system components,
disposition of data and documentation, and updates to system inventory records
where appropriate.
6.7.3 Disposition of the Data and Documentation: Prior to decommissioning of a system,
all the data contained within is either destroyed, archived, or migrated to a new
system depending on the business need. When a system is decommissioned, all
system-related documentation is reviewed and archived based upon contractual
agreements and regulatory requirements.
6.7.4 The system Retirement Report is written by the IT CSV and summarizes the
results from the execution of the System Retirement Plan.
7 ATTACHMENTS
• FRM-012-01 IT Change Control Form
8 REVISION HISTORY
Version Number Date Summary of Change(s)
01 22-MAY-2026 New Document
[X.0] [DD-MMM-YYYY] [Insert a summary of the changes]
SIGNATURE PAGE
[ADD ADDITIONAL ROWS AS NEEDED]
Author:
NAME TITLE SIGNATURE DATE
Justin Shaka Fractional COO
Reviewer:
NAME TITLE SIGNATURE DATE
Jay Chhablani President
Approver:
NAME TITLE SIGNATURE DATE
Sandeep Chandra
Director of AI
Bollepalli
