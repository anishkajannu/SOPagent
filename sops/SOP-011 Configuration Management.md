# SOP-011 — Configuration Management

1 PURPOSE
This Standard Operating Procedure (SOP) describes the policies and procedures for Configuration
Management of systems maintained and supported by Netramind for GxP operations.
These policies and procedures will provide a consistent, acceptable and defined standard for
Configuration of computerized systems and associated artifacts. Following this procedure will
eliminate the likelihood of confusion and errors brought about by having multiple versions of artifacts
that are not managed in a change control standard practice and are compliant with regulations.
2 SCOPE
This procedure applies to computerized systems, software artifacts, and controlled documentation
maintained and supported by Netramind in support of GxP-regulated activities.
This procedure applies to all employees, contractors and vendors implementing or using
computerized systems.
3 REFERENCES
• SOP-010 Software Development Lifecycle
• SOP-008 Incident Management
• SOP-012 IT Change Control
• FRM-012-01 IT Change Control Form
• European Medicines Agency (EMA): EudraLex Volume 4, Part 1: Basic Requirements for
Medicinal Products; Annex 11: Computerized Systems
• European Medicines Agency (EMA): Guideline on computerized systems and electronic data in
clinical trials
• Food and Drug Administration (FDA): 21 CFR Part 11; 21 CFR parts 210 and 211 and 820
• International Conference on Harmonization (ICH) Q7: Good Manufacturing Practice Guide for
Active Pharmaceutical Ingredients; November 2000
• International Conference on Harmonization (ICH) E6 (R3) Good Clinical Practice
• GAMP 5: A Risk-Based Approach to Compliant GxP Computerized Systems
4 DEFINITIONS
4.1 Artifact— An artifact may be a piece of hardware, software or documentation.
4.2 Configuration Management (CM) — The process of maintaining consistency, integrity,
version control, and traceability of computerized systems and associated artifacts
throughout their lifecycle.
4.3 Computer System— A functional unit, consisting of one or more computers and
associated peripheral input and output devices, and associated software, that uses
common storage for all or part of a program and also for all or part of the data necessary
for the execution of the program; executes user-written or user-designated programs;
performs user-designated data manipulation, including arithmetic operations and logic
operations; and that can execute programs that modify themselves during their execution.
A computer system may be a stand-alone unit or may consist of several interconnected
units.
4.4 Computerized System— The set of hardware, software, peripheral devices, personnel,
and documentation needed to perform a specific group of functions to meet a business or
regulatory need. A Computer System (defined above) is a component of a Computerized
System.
4.5 External Service Provide (ESP) — A person or organization providing services to, but
not directly employed by Netramind.
4.6 Incident Report (IR) — An official report of an identified incident found in the
computerized system. All IRs are required to follow SOP-008 Incident Management.
4.7 Release Management— The process of managing, planning, scheduling and controlling
software builds through different stages and environments.
4.8 Software Development Lifecycle (SDLC) — The model that defines the phases and
procedures for the process of defining, developing, testing, maintaining, and retiring
systems. Several phases exist in the SDLC, which support successful software
development and maintenance. The phases are definition, development, validation, and
production/maintenance.
4.9 Source Management— Source management is the activity that controls version
management of source code, access to source code, and tracking changes. These
activities are put in place to ensure the integrity of the code and traceability of changes.
4.10System Owner— Individual who has the functional responsibility for the system; for
providing the data or function that the computerized system addresses, known as user
requirements. It is possible that different parts of a complex integrated system would
have multiple System Owners.
4.11Version Control and Management— The activities involved in providing an environment
where builds are created, storage of source code, and assigning unique version names or
numbers to unique states of computer software and files.
5 RESPONSIBILITIES
5.1 System Owner or Designee
5.1.1 Reviewing and approving validation documents as required.
5.1.2 Ensuring the system is appropriate for its intended purpose.
5.1.3 Ensuring changes to a validated system are performed per formal change control
procedures.
5.1.4 Developing and ensuring controlled documentation follows the CM policies and
procedures.
5.2 Users
5.2.1 Following CM procedures and maintaining only current versions of controlled
documents.
5.3 Quality Assurance (QA) System Validation or Designee
5.3.1 Ensures configuration management practices are documented and followed for
controlled systems and artifacts.
5.4 Development Team or Designee
5.4.1 Developing and ensuring controlled documentation follows the CM policies and
procedures.
5.4.2 Complies with source and release management policies and procedures.
5.5 Technical Team/Information Technology Team (IT) or Designee
5.5.1 Provides technical infrastructure as per system requirements.
5.5.2 Responsible for installing and configuring version control systems.
5.5.3 Performs release management activities.
5.5.4 Reviewing and approving validation documents as required.
5.6 Developing and ensuring controlled documentation follows the CM policies and
procedures.
6 PROCEDURE
6.1 Process Overview
6.1.1 Configuration management activities may include planning, version control,
source management, documentation control, release management, and
communication of approved changes.
6.2 Planning & Definition
6.2.1 Identify what artifacts will be under control of CM.
6.2.2 Appropriate software, documentation, and system artifacts are identified and
maintained under configuration management control.
6.2.3 Define a version tracking methodology for each artifact.
6.2.4 Define a naming convention for each artifact.
6.2.5 Configuration management approaches are reviewed as appropriate based on
system risk and intended use.
6.3 Version Control
6.3.1 Source Code
6.3.1.1 Source code is maintained in controlled version management systems with
appropriate access control and traceability of changes.
6.3.1.2 Significant changes to controlled or production systems are managed
through change control procedures.
6.3.2 Documentation
6.3.2.1 Documents that have a unique occurrence do not require continuous
maintenance and/or updates.
• Examples are:
• CCRs
• IRs
6.3.2.2 Controlled records may be maintained in issue tracking or document
management systems with appropriate traceability and access controls.
6.3.2.3 Controlled documents that are continuously maintained in version control
much like source control.
• Examples of these artifacts are:
• Specifications
• Policies and Procedures
• Validation documentation
6.3.2.4 Each artifact is stored in a controlled environment enabled with access
control. Only individuals with the permission to view and/or edit are
allowed.
6.3.2.5 Controlled documents that are being edited have track changes on and/or
the documentation system tracks changes as they are made. If there are
two individuals editing a document both changes are saved and prompted
for review and/or merge.
• A history of the changes to the document is saved in the system and
available for reference if required.
6.3.2.6 Each controlled artifact is reviewed and approved prior to being issued.
6.3.2.7 Approved documents that are amended require re-approval and the old
version to be made obsolete when the new version is approved.
6.3.2.8 Approved documents are labeled with a version identifying that it is
approved, issued, and made available to all who require access to the
document.
• The obsolete version is removed from being accessible.
6.3.2.9 All versions of documents are in the document repository for reference
and historical purposes. Only the latest approved version is accessible.
6.3.2.10Document naming convention is as follows:
• DocType-uniqueId-Version#- Name
• Where as:
• DocType – lists the type of document ex: SOP, TSTPlan, etc.
• UniqueId – Document id listed in master document list ex: CSV - 103
• Version# - what revision the document is ex: 01
• Name – Configuration Management
6.3.2.11All validation and SDLC documentation containing the results of activities
that occurred are considered static and historical in nature. These results
of the activities are stored in compliance with Record Retention policies.
6.4 Release Management
6.4.1 The Release Management Process ensures that all releases are properly verified
and documented according to plan. All releases of software are performed in
accordance to the SOP-010 Software Development Lifecycle process.
6.5 Communication
6.5.1 Updated versions of approved software and controlled artifacts are communicated
to relevant personnel as appropriate.
6.5.2 When a new version is replacing an old version a communication is made to
reference the new version and to instruct all copies of the old version to be
replaced with the new version.
7 ATTACHMENTS
• N/A
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
