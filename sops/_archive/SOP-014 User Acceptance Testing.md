# SOP-014 — User Acceptance Testing

1 PURPOSE
The purpose of this Standard Operating Procedure (SOP) is to describe the policies and procedures for
performing User Acceptance Testing on all GxP systems maintained and supported by Netramind
and/or all systems provided by ESP(s), including verification that systems support protocol-defined
image review workflows, grading, adjudication, and generation of clinical trial endpoints.
2 SCOPE
This procedure applies to UAT activities for GxP systems used to ingest, process, analyze, and report
ophthalmic imaging data in support of clinical trials.
3 REFERENCES
• FDA Guidance for Industry: Part 11, Electronic Records; Electronic Signatures – Scope and
Application; 21 CFR Part 11 Electronic Records and Electronic Signatures
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
4.1 Acceptance Criteria— The established standard that a system or component must satisfy for a
result to be acceptable to the user, customer or other authorized entity.
4.2 Change Control Request (CCR) Form— An official request for prospective approval to implement
a change to a validated system.
4.3 Configuration—Criteria to set up a system using existing (out-of-the-box) functionality.
4.4 Data Acquisition Tool (DAT) —A paper or electronic tool designed to collect data and associate
metadata with a data originator in a clinical trial according to the protocol and to report the data
to the sponsor. The data originator may be a human (e.g., the participant or trial staff), a
machine (e.g., wearables and sensors), or a computer system from which the electronic transfer
of data from one system to another has been undertaken (e.g., extraction of data from an
electronic health record or laboratory system). Examples of DATs include but are not limited to
CRFs, interactive response technologies, clinical outcome assessments, including patient-
reported outcomes (PROs) and wearable devices, irrespective of the media used.
4.5 Functional Specifications— Functional Specification document describes the Computerized
System in terms of the functions it will perform and facilitates required to meet the User
Requirements. They also document the fundamental processes or transformations that the
Computerized System performs on inputs to produce outputs.
4.6 Functional Requirements Specification (FRS)— Functional requirements contain User
Requirements and Functional Specifications. It describes the Computerized System in terms of
the functions it will perform, and facilities required to meet the User Requirements. They also
document the fundamental processes or transformations that the Computerized System
performs on inputs to produce outputs.
4.7 Installation Qualification (IQ)— The documented verification testing to confirm the installation of
hardware and software was successful. It typically verifies system parameters are set, any
necessary file structures, directories and/or databases are present, proper security profiles are
established, interfaces to other systems are connected properly (e.g., other programs or
hardware, such as printers), and all application menus, buttons, and drop downs, as applicable,
are functioning in conformance with the application user manual and any applicable updates.
4.8 Interface—A system, device or other entity that provides input or output for a computerized
system but is not considered being within the design boundary of the computerized system.
4.9 Metadata—The contextual information required to understand a given data element. Metadata
is structured information that describes, explains, or otherwise makes it easier to retrieve, use,
or manage data to allow for the appropriate evaluation of the trial conduct.
4.10Operational Qualification (OQ)— A prospective plan that when executed is intended to produce
documented evidence that a system or subsystem has been properly qualified. Documented
verification that a system meets its Functional Specification (FS).
4.11Performance Qualification (PQ)— The documented verification that the facilities, systems, and
equipment, as connected, can perform effectively and reproducibly, based on the approved
process method and product specification. Documented verification that a system meets its User
Requirements (UR).
4.12Process / Business Owner—The person ultimately responsible for the business process or
processes being managed. The process owner is responsible for ensuring that the computerized
system and its operation comply and fit for intended use in accordance with applicable Standard
Operating Procedures (SOPs) throughout its useful life. Responsibility for control of system
access should be agreed between process and system owner. In some cases, the process owner
also may be the system owner.
4.13Subject Matter Expert (SME)— individuals with highest level of expertise/competency in skills or
performing specialized tasks who can provide specific detailed knowledge or expertise.
4.14Traceability Matrix (TM)— A matrix that maps the specification requirements to the test scripts
verifying that the specification was met.
4.15User Requirements Specification (URS)—Document that describes what the equipment or
system is supposed to do and is normally written by the user. The UR includes all essential
requirements, and a prioritized list of desirable requirements. Requirements should be linked to
the PQ, which tests the system in its operating environment, including the associated
procedures.
4.16User Acceptance Testing (UAT) —A phase of testing in which users test the electronic system to
ensure it can handle required tasks according to user requirement specifications
5 RESPONSIBILITIES
5.1 Business Owner or Designee
5.1.1 Function as Subject Matter Expert (SME) responsible for defining the intended use of
computerized system and defining the scope of UAT.
5.1.2 Maintaining a system in its validated state.
5.1.3 Review and approve the system validation documentation.
5.1.4 Contribute and approve risk assessments for GAMP, GxP, 21 CFR Part 11 applicability.
5.1.5 Ensure changes to the validated system are documented through a formal change control
procedure.
5.1.6 Develop SOP for the intended use of the validated system.
5.2 Quality Assurance (QA) or Designee
5.2.1 Establish validation strategy and provide quality oversight for validation activities.
5.2.2 Ensure validated systems adhere to regulatory standards.
5.2.3 Perform GAMP, GxP, 21 CFR Part 11 applicability assessment.
5.2.4 Evaluate systems for compliance with applicable regulations.
5.2.5 Ensure that validation documentation and execution follow good documentation
Practices.
5.2.6 Review and approve UAT plans and summary reports and provide oversight of UAT
activities.
5.3 End Users or Designee
5.3.1 End Users may include trained graders, adjudicators, reading center managers, and data
reviewers.
5.3.2 Provide input into UAT strategy.
5.3.3 Provide input to improve system performance to meet the intended use.
5.3.4 In the validation process SME can be from any relevant department including Business,
Training, Validation, QA, and IT departments.
5.4 IT or Designee
5.4.1 Technical team is responsible for providing infrastructure as per system requirements.
5.4.2 Responsible for installing and configuring system environments.
5.4.3 Responsible for providing technical support during validation activities.
5.4.4 Evaluate any system related risks and errors during implementation of the system.
5.4.5 IT department will maintain the IT Regulated Systems List.
6 PROCEDURE
6.1 Planning
6.1.1 The BO of the system reviews the requirements, traceability matrix and validation plan to
assess the scope and resources required to perform UAT testing.
6.1.2 A UAT Test Plan is written to describe the testing which will be performed during UAT
testing. For systems supporting multiple clinical studies, UAT may be performed at the
study configuration level to verify protocol-specific workflows, data handling, and output
requirements.
6.1.3 Test Scripts will be documented in accordance with the UAT Test Plan. The scripts will
contain test steps, expected results; actual results, tester initials or signature and date
test step was executed.
6.1.4 End user SOPs and WIs should be reviewed to determine any impact on daily operations.
If there are changes that impact job processes, all documentation requiring updates
should be done prior to UAT testing.
6.1.5 Training documentation should be updated when there are changes to operations.
6.2 Testing
6.2.1 The intent of the UAT is to verify that the configurations and / or enhancements can
perform the activities of the business process.
6.2.2 Where applicable, prerequisite testing (e.g., system or functional testing) must be
completed prior to UAT. Successful IQ and OQ are prerequisites to performing PQ.
6.2.3 UAT is performed by trained users in collaboration with the technical team to verify that
the intended use of the system/change is met.
6.2.4 Testers will use good documentation practices.
6.2.5 Quality Assurance must pre-approve all Plans, Protocols, and Reports.
6.2.6 Appropriate screen prints will be provided to demonstrate results of critical test steps or
errors.
6.2.7 Deviations will be documented, investigated, and evaluated for corrective action or
acceptance.
6.2.8 Executed scripts will not be discarded
6.2.9 For severe deviations, testing will be halted, and an assessment will be made as to how to
proceed with UAT and review the implications to the validated state.
6.2.10 Upon completion of UAT testing cycle, the following UAT acceptance criteria must be met.
6.2.10.1 UAT test cases must be executed and passed successfully or documented in the
Release Notes if not successful.
6.2.10.2 Documentation specified in the applicable change record must be approved
before deployment of the change to the validation or production instance.
6.2.10.3 The Change Control Team approves the change control
6.3 Review
6.3.1 The UAT Summary Report captures the overall result of the UAT testing and any
deviations that occurred.
6.3.2 The UAT Summary Report includes:
6.3.2.1 States if the system meets the acceptance criteria as listed in the UAT plan.
6.3.2.2 List of all documents created as a part of the validation of the system
6.3.2.3 A high-level summary of the validation testing
6.3.2.4 Environments in which testing occurred
6.3.2.5 Any exceptions / deviation to the UAT Plan
6.3.2.6 List of any outstanding issues identified post going live
7 ATTACHMENTS
• N/A
8 REVISION HISTORY
Version Number Date Summary of Change(s)
01 01-MAY-2026 New Document
[X.0] [DD-MMM-YYYY] [Insert a summary of the changes]
SIGNATURE PAGE
[ADD ADDITIONAL ROWS AS NEEDED]
Author:
NAME TITLE SIGNATURE DATE
Justin Shaka Fractional COO 01-MAY-2026
Reviewer:
NAME TITLE SIGNATURE DATE
Approver:
NAME TITLE SIGNATURE DATE
