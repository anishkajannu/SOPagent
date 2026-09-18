# SOP-010 — Software Development Lifecycle

1 PURPOSE
This Standard Operating Procedure (SOP) describes the policies and procedures for all phases of the
Software Development Lifecycle of computerized systems developed, maintained and supported by
Netramind for GxP operations.
These policies and procedures provide a consistent, acceptable and defined standard as applied to
the definition, design, build, use, modification, maintenance, and retirement of computerized
systems. Following this procedure helps ensure computerized systems operate according to their
intended use, support reliable data handling, and maintain appropriate controls for GxP activities.
2 SCOPE
This SOP applies to computerized systems developed, configured, maintained, or used by Netramind
in support of GxP-regulated activities, including systems involved in clinical data analysis and related
workflows.
3 REFERENCES
• SOP-013 Computer System Validation
• SOP-004 GxP Records Retention
• SOP-008 Incident Management
• SOP-012 IT Change Control
• FDA Guidance for Industry: Part 11, Electronic Records; Electronic Signatures – Scope and
Application; 21 CFR Part 11 Electronic Records and Electronic Signatures
• ICH E6(R3): Guidelines for Good Clinical Practice (GCP), Section 5.5.3
4 DEFINITIONS
4.1 Acceptance Criteria— The established standard that a system or component must satisfy
for a result to be acceptable to the user, customer or other authorized entity.
4.2 Computer System—A functional unit, consisting of one or more computers and
associated peripheral input and output devices, and associated software, that uses
common storage for all or part of a program and also for all or part of the data necessary
for the execution of the program; executes user-written or user-designated programs;
performs user-designated data manipulation, including arithmetic operations and logic
operations; and that can execute programs that modify themselves during their execution.
A computer system may be a stand-alone unit or may consist of several interconnected
units.
4.3 Computerized System—The set of hardware, software, peripheral devices, personnel, and
documentation needed to perform a specific group of functions to meet a business or
regulatory need. A Computer System (defined above) is a component of a Computerized
System.
4.4 Computerized Systems Validation (CSV)—A process of establishing and documenting that
the specified requirements of a computerized system can be consistently fulfilled from design
until decommissioning of the system or transition to a new system. The approach to
validation should be based on a risk assessment that takes into consideration the intended use
of the system and the potential of the system to affect trial participant protection and the
reliability of trial results.
4.5 Electronic Record —Any combination of text, graphic, data, audio, pictorial, or other
information representations in digital form that is created, modified, maintained,
archived, retrieved, or distributed, by a computer system. A system transaction or data set
is not considered to be an electronic record until the data entry is committed to a
database.
4.6 Electronic Signature —A computer data compilation of any symbol or series of symbols
executed, adopted, or authorized by an individual to be legally binding, legally equivalent
to the individual’s handwritten signature.
4.7 End User— The final or ultimate user of a computer system. An end user is an individual
who uses the product for its intended purpose after it has been fully developed and
marketed. A System Administrator is not considered to be an End User.
4.8 Functional Requirements Specification (FRS)— The Functional requirements contain
User Requirements and Functional Specifications. It describes the Computerized System
in terms of the functions it will perform, and facilities required to meet the User
Requirements. They also document the fundamental processes or transformations that
the Computerized System performs on inputs to produce outputs.
4.9 Incident(s)— Any unexpected issue, error, malfunction, or failure associated with a
computerized system or related process. During the build phase of the SDLC incidents
are discovered and reported in an incident report. Incidents that are deemed part of
release criteria are corrected and retested during the Build phase. If incidents discovered
are determined to be new requirements, they are required to follow SOP-012 IT Change
Control.
4.10Incident Report (IR)— An official report of an identified incident found in the
computerized system.
4.11Software Development Lifecycle (SDLC)— The model that defines the phases and
procedures for the process of defining, developing, testing, maintaining, and retiring
systems. Several phases exist in the SDLC, which support successful software
development and maintenance. The phases are definition, development, validation, and
production/maintenance.
4.12System Design Specification (SDS)— System Design Specification captures the design
of a system or system component to satisfy specified requirements.
4.13System Owner— Individual who has the functional responsibility for the system; for
providing the data or function that the computerized system addresses, known as user
requirements. It is possible that different parts of a complex integrated system would
have multiple System Owners.
4.14User— Netramind employees, consultants, and contract employees who access the
systems and applications.
4.15User Requirements Specification (URS)— A document that defines the user’s needs, but
generally not a specific technical solution.
4.16Validation— Establishing documented evidence that provides a high degree of assurance
that a specific computerized system will consistently operate in accordance with pre-
determined specifications and continues to operate as specified throughout its system
lifecycle.
4.17Validation Plan (VP) — A formal document providing a framework that describes the
validation process, responsibilities, documentation deliverables, timelines, acceptance
criteria and maintenance of the validated state for a given computerized system. The VP
encompasses the system’s lifecycle (development, implementation, use and retirement).
4.18Version Control and Management— The activities involved in providing an environment
where builds are created, storage of source code, and assigning unique version names or
numbers to unique states of computer software and files.
5 RESPONSIBILITIES
5.1 Project Manager (PM)
5.1.1 Coordinates project activities and timelines.
5.1.2 Facilitates communication between functional groups.
5.2 System Owner
5.2.1 Ensures the system remains appropriate for intended use.
5.2.2 Supports maintenance, validation, and change activities as appropriate.
5.3 Users
5.3.1 Uses systems according to approved procedures.
5.3.2 Reports issues or incidents as appropriate.
5.4 Quality Assurance (QA)
5.4.1 Ensures appropriate SDLC documentation and controls are maintained.
5.4.2 Reviews validation and change activities where applicable.
5.5 Development Team
5.5.1 Develops and maintains systems according to approved requirements and
development practices.
5.5.2 Performs appropriate testing and version control activities.
5.6 Technical Team/Information Technology Team (IT)
5.6.1 Supports system infrastructure, deployment, and technical maintenance activities.
6 PROCEDURE
This section describes the System Development Life Cycle (SDLC) and the activities that are required
to plan, define, build, deploy, maintain, and retire a computerized system.
6.1 Planning
6.1.1 The project plan is developed including timelines, budget, and resources required
to successfully complete the plan.
6.1.1.1 The plan is managed throughout by the PM.
6.1.1.2 The PM ensures all phases are completed successfully.
6.1.2 GxP Assessment is performed to determine whether the system requires validation.
6.1.3 21 CFR Part 11 Assessment is performed to determine compliance with 21 CFR
Part 11 using the FRM-01-01 21 CFR part 11 Assessment form.
6.1.4 A validation approach may be defined based on system risk, intended use, and
regulatory relevance.
6.1.5 SOP and or Work Instructions for using the system, system access, data security,
system/data backup and recovery, and periodic maintenance activities.
6.2 Definition
6.2.1 URS - The URS initially drafted during the planning phase is reviewed and
finalized.
6.2.1.1 UR Identifier: Unique requirement number is required for each
requirement for an easy reference.
6.2.2 FRS – The FRS is authored based upon the URS. In some cases, the URS and
FRS may be combined into one document. This will be defined and justified in the
VP. At a minimum the FRS should include the following:
6.2.2.1 Data and/or process flow diagrams
6.2.2.2 Data and metadata definitions
6.2.2.3 Descriptions of functions
6.2.2.4 FR Identifier: Unique requirement number is required for each
requirement for an easy reference and must map to at least one user
requirement.
6.2.3 SDS – The SDS is authored based upon the URS & FRS. At a minimum the SDS
should include the following:
6.2.3.1 List of hardware components
6.2.3.2 List of software components
6.2.3.3 System Landscape diagram
6.2.3.4 Database schema, if applicable
6.2.3.5 Interfaces, if applicable (devices and/or other computerized systems.
6.2.4 When the design is completed, the URS, FRS and SDS are approved and are
subject to formal change control.
6.2.5 Where applicable, data migration activities are planned and documented
appropriately.
6.2.6 At a minimum SOPs or IT Work Instructions will be written to address:
6.2.6.1 Use and administration of the system
6.2.6.2 Data and system backup and recovery
6.2.6.3 Data and system access and security
6.2.6.4 System maintenance and change control
6.2.7 If SOPs already exist, review the SOPs appropriateness and modify if needed. The
SOPs must be approved prior to the approval of the VSR.
6.3 Build
Change Control Management process is initiated in the build phase. Change Control
Management appropriately manages the definition and approval of any changes to the system
that were not previously identified in the User Requirements or Design Specification. Refer to
SOP-012 IT Change Control for more details.
6.3.1 Development
6.3.1.1 Systems are developed according to defined requirements and appropriate
development practices, including version control and testing activities.
6.3.2 Source Management
6.3.2.1 Source code and related artifacts are maintained in controlled version
management systems with appropriate access controls and traceability of
changes.
6.3.3 Release Management
6.3.3.1 Releases are managed in a controlled manner prior to deployment into
production environments.
6.3.4 QA System & Integration
6.3.4.1 Appropriate testing activities are performed prior to production
deployment. Issues identified during testing are documented and managed
through the Incident Management process.
6.3.5 Validation Testing
6.3.5.1 Validation and testing activities are performed based on system risk and
intended use to provide reasonable assurance that systems function as
intended.
•
6.4 Incident Management
6.4.1 The Incident Management process ensures that all identified incidents are properly
documented, reviewed, approved or rejected, and fixes are planned according to
severity and priority. Incident Management is performed in accordance with SOP-
008 Incident Management.
6.5 Change Control Management
6.5.1 Changes to controlled or production systems are managed through the IT Change
Control process. Change Control is performed in accordance with SOP-012 IT
Change Control.
6.5.2 Significant changes to controlled or production systems are managed through
change control procedures.
6.6 Production Deployment
6.6.1 Systems are deployed to production following completion of appropriate testing,
approvals, and readiness activities.
6.7 Maintenance
6.7.1 Systems are maintained through ongoing support, issue management, and change
control activities as appropriate.
6.8 Retirement
6.8.1 When management has determined that a system is to be obsoleted, replaced or
upgraded, the action of retiring the system must be initiated through change
control.
6.8.2 System retirement activities include consideration of data retention, archival,
access, and disposition of system components where applicable.
7 ATTACHMENTS
• FRM-015-01 21 CFR part 11 Assessment Form
2
3
8 REVISION HISTORY
Version Number Date Summary of Change(s)
01 22-MAY-2026 New Document
[X.0] [DD-MMM-YYYY] [Insert a summary of the changes]
SIGNATURE PAGE
[ADD ADDITIONAL ROWS AS NEEDED]
Author:
NAME TITLE SIGNATURE DATE DD-MMM-YYYY
Justin Shaka Fractional COO
Reviewer:
NAME TITLE SIGNATURE DATE
Jay Chhablani President
Approver:
NAME TITLE SIGNATURE DATE
Sandeep Chandra
Director of AI
Bollepalli
