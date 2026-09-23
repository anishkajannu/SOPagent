# SOP-021 — IT System Adminstration and Maintenance

1 PURPOSE
This SOP outlines the administration and maintenance of computerized systems used by Netramind to
support GxP activities, ensuring systems remain controlled, secure, and fit for intended use.
2 SCOPE
This procedure applies to GxP-relevant computerized systems maintained or used by Netramind,
including internally managed and externally hosted systems.
3 REFERENCES
• SOP-010 Software Development Lifecycle
• SOP-008 Incident Management
• SOP-014 Computer System Validation
• SOP-017 Audit Trail Review
• SOP-025 Periodic Review of IT Systems
• SOP-019 User Access Management
• 21 CFR (Code of Federal Regulations) PART 11 Electronic Records; Electronic Signatures
4 DEFINITION S
4.1 Audit Trail—Metadata records that allow the appropriate evaluation of the course of events by
capturing details on actions (manual or automated) performed relating to information and data
collection and, where applicable, to activities in computerized systems. The audit trail should
show activities, initial entry and changes to data fields or records, by whom, when and, where
applicable, why. In computerized systems, the audit trail should be secure, computer-generated
and time stamped.
4.2 Corrective and Preventive Action (CAPA)— A systematic approach that includes actions needed
to correct (“correction”), prevent recurrence (“corrective action”), and eliminate the cause of
potential nonconforming product and other quality problems (preventive action).
4.3 Change Control—A general term describing the process of managing how changes are
introduced into a controlled system.
4.4 Computerized System—The set of hardware, software, peripheral devices, personnel, and
documentation needed to perform a specific group of functions to meet a business or regulatory
need. A Computer System (defined above) is a component of a Computerized System.
4.5 Data Acquisition Tool (DAT) — A paper or electronic tool designed to collect data and associated
metadata from a data originator in a clinical trial according to the protocol and to report the data
to the sponsor. The data originator may be a human (e.g., the participant or trial staff), a
machine (e.g., wearables and sensors) or a computer system from which the electronic transfer
of data from one system to another has been undertaken (e.g., extraction of data from an
electronic health record or laboratory system). Examples of DATs include but are not limited to
CRFs, interactive response technologies (IRTs), clinical outcome assessments (COAs), including
patient-reported outcomes (PROs) and wearable devices, irrespective of the media used.
4.6 End User— The final or ultimate user of a computer system. An end user is an individual who
uses the product for its intended purpose after it has been fully developed and marketed. A
System Administrator is not considered to be an End User.
4.7 Firmware— A type of software program embedded into hardware devices to help the devices’
function, so the combination of a hardware device and computer instructions/data that resides
as read only software on that device. The software may or may not be configurable. The
computer cannot modify such software during processing.
4.8 Incident Report (IR) — An official report of an identified incident found in the computerized
system.
4.9 Interface— A system, device or other entity that provides input or output for a computerized
system but is not considered to be within the design boundary of the computerized system.
4.10Metadata— The contextual information required to understand a given data element. Metadata
is structured information that describes, explains or otherwise makes it easier to retrieve, use or
manage data. Relevant metadata are those needed to allow the appropriate evaluation of the
trial conduct.
4.11Production Environment—This is the environment used for normal business use. The system is
used to create, store, modify and or transfer GxP data. The environment is controlled so that all
changes to the environment are documented.
4.12Regression Testing—A test performed meant to verify that software previously developed and
working is still working correctly after it was changed.
4.13Release Management —The process of managing, planning, scheduling and controlling software
builds through different stages and environments.
4.14Root Cause Analysis (RCA)— The process of identifying the causal factors of noncompliance, a
deviation, violation, or undesirable outcome.
4.15Service Level Agreement (SLA)— A contract between a service provider and customer that
defines the service to be provided, and the level of performance expected and measured. SLAs
are typically in place for IT service providers.
4.16Software as a Service (SaaS) – Applications which are hosted by a service provider and are made
available to users on a subscription basis, eliminating the need for local installation and
infrastructure management. Netramind still is responsible for qualifying the service provider of
SaaS applications including verification that IQ and OQ were sufficiently executed by the SaaS
service provider and performing a risk-based validation based on user requirements, as the
regulatory responsibility for ensuring and demonstrating the integrity of GxP data in the SaaS
solution remains with Netramind.
4.17Software Development Lifecycle (SDLC) — The model that defines the phases and procedures for
the process of defining, developing, testing, maintaining, and retiring systems. Several phases
exist in the SDLC, which support successful software development and maintenance. The phases
are definition, development, validation, and production/maintenance.
4.18System Administrator— Individual who has the functional responsibility for the system; for
providing the data or function
4.19System Owner— Individual who has the functional responsibility for the system; for providing
the data or function that the computerized system addresses, known as user requirements. It is
possible that different parts of a complex integrated system would have multiple System
Owners.
4.20Traceability Matrix (TM) — A matrix that maps the specification requirements to the test scripts
verifying that the specification was met.
4.21Uninterruptable Power Supply (UPS) — A device that allows a computer to keep running for at
least a short time when the primary power source is lost. It also provides protection from power
surges.
4.22Validation— Establishing documented evidence that provides a high degree of assurance that a
specific computerized system will consistently operate in accordance with pre-determined
specifications and continues to operate as specified throughout its system lifecycle.
4.23Validation Plan (VP)— A formal document providing a framework that describes the validation
process, responsibilities, documentation deliverables, timelines, acceptance criteria and
maintenance of the validated state for a given computerized system. The VP encompasses the
system’s lifecycle (development, implementation, use and retirement).
4.24Validation Summary Report (VSR) — A document that summarizes the validation activities,
exceptional conditions occurring during testing and the justification for releasing for use or
continued use of the system.
5 RESPONSIBILITIES
5.1 System Owner
5.1.1 Maintain the validated state of the system.
5.1.2 Review and approving validation documents as required.
5.1.3 Ensure changes to a validated system are performed via formal change control
procedures.
5.1.4 Ensure specification documentation is up to date, and consistent with the needs of the
system’s users.
5.1.5 Define scope of maintenance releases.
5.1.6 Develop and/or update SOPs for the intended use of the validated system.
5.1.7 Ensure the performance of validation activities according to this SOP, including the
conduction and documentation of validation testing.
5.2 Users
5.2.1 Follow change control procedures.
5.2.2 Report system problems or failures to the System Owner or IT as appropriate.
5.2.3 Support validation activities as needed.
5.3 Quality Assurance (QA) Validation
5.3.1 Review and approve validation activities and ensure compliance.
5.3.2 Manage incident tracking.
5.3.3 Review and approve all testing and validation documents.
5.3.4 Summarize the results of all testing in a VSR.
5.3.5 Support Production Deployment.
5.3.6 Evaluate systems for compliance with applicable and current regulations for
computerized systems and data integrity.
5.4 Development Team
5.4.1 Prepare and/or maintain up to date functional and design requirements to satisfy the
user’s requirements.
5.4.2 Develop the system to satisfy the required specifications.
5.4.3 Execute peer code review, unit and integration tests following development best practices
and standards.
5.4.4 Comply with source and release management policies and procedures.
5.4.5 Support testing, validation, production deployments, and post-production deployment.
5.5 Technical Team/Information Technology Team (IT)
5.5.1 Provide technical infrastructure as per system requirements.
5.5.2 Responsible for installing and configuring system environments.
5.5.3 Perform release management activities.
5.5.4 Provide technical support during validation activities.
5.5.5 Maintain the system in accordance with its validated state.
5.5.6 Review and approving validation documents as required.
5.5.7 Evaluate any system related risks and errors during implementation of the system and
post-production deployment.
6 PROCEDURE
6.1 General System Administration and Support
6.1.1 All support and change requests for IT systems, Netramind-developed or SaaS based
services are managed through a Change Request process according to FRM-021-01 IT
Change Control.
6.1.2 Account Management and Access Control
6.1.2.1 User access, change/update and removal of access procedures are described in
SOP-019 User Account Management.
6.1.3 System Release Updates
6.1.3.1 System updates from internal or external providers must be assessed and
managed through change control, as appropriate.
6.1.4 IT performs any standard change to the specific system following FRM-
021-01 IT Change Control. Standard changes include changes to
controlled terminology and/or routine maintenance.
6.1.5 Major changes to the specific system adhere to the procedures defined in
SOP-ABC-123 Software Development Lifecycle.
6.1.6 IT Help Desk Support
6.1.6.1 Netramind utilizes the IT Help Desk function, either resourced internally or
delegated to a third-party technology support service provider, to manage
requests related to technology, systems software and hardware components.
6.1.6.2 The IT Help Desk technical staff is responsible for evaluating, resolving, tracking
and closing help desk support tickets.
6.1.7 IT Service Level Agreement (SLA)
6.1.7.1 SLAs are established between service/technical providers for systems which are
not developed or managed internally by Netramind IT. Security expectations
such as authentication controls (e.g., MFA) should be defined where applicable.
6.1.7.2 IT and System Owner are responsible for the relationship with the providers,
including reviewing and approving the criteria defined in the SLA, including
expectation for system administration and system maintenance.
6.1.7.3 IT and System Owner are responsible for the oversight of the service provider to
ensure tasks are executed according to the criteria agreed to in the SLA.
6.2 System Maintenance Planning
6.2.1 The System Owner reviews all approved change requests to current operational system
and open incidents to define maintenance releases.
6.2.2 All maintenance releases and deliverables must comply with procedures defined in SOP-
010 Software Development Lifecycle.
6.2.3 Change Impact Assessment
6.2.3.1 Changes must be assessed for impact on system functionality, data integrity, and
validation status. Appropriate testing and documentation updates must be
defined based on this assessment.
6.2.4 Technical Change Development
6.2.4.1 The changes are built per the specifications, Change Control Request (CCR)
and/or Incident Report (IR).
6.2.4.2 All technical changes to the system are documented in development notes for
each FRM-021-01 IT Change Control Form and/or FRM-021-02 Incident Request
Form. All changes must follow applicable SOPs on SDLC and Incident
Management.
6.2.5 Change Control
6.2.5.1 Change Control ensures that proposed changes to computer systems will be
properly documented, reviewed, evaluated, approved or disapproved/rejected,
and implemented, and that approved changes shall be communicated to the
appropriate personnel in a timely manner.
6.2.5.2 Execute change control in accordance with FRM-021-01 IT Change Control Form.
6.2.6 Validation
6.2.6.1 System testing will be performed to ensure there are no major issues with the
system prior to releasing the system for validation & qualification testing.
6.2.6.2 Validation & qualification testing will be executed following the standards in
SOP-014 Computer System Validation.
6.2.7 Regression Testing
6.2.7.1 Regression testing is performed to satisfy the tasks identified in the Validation
Plan (VP).
• Rerun identified test cases previously executed
• Identify any unintended effects of the system changes
6.3 Technical Release Management
6.3.1 The system release plan is determined in accordance with procedures described in SOP-
010 Software Development Lifecycle.
6.4 Incident Management
6.4.1 All identified incidents during technical change implementation are properly
documented, reviewed, approved or rejected, and fixes are planned according to severity
and priority. Incident Management is performed in accordance with SOP-008 Incident
Management.
6.5 Hardware Maintenance
6.5.1 Hardware supporting GxP systems must be maintained through preventative
maintenance, monitoring, and timely updates to ensure reliability and performance.
6.6 Periodic Reviews
6.6.1 Review of specific system requirements, processes are specified in the Validation Plan and
should be incorporated into the planned periodic reviews of the systems, for example:
issues are discovered during the Periodic review, a gap analysis will be performed to
establish a remediation plan. The remediation plan will be executed according to FRM-
021-01 IT Change Control Form procedure.
6.6.2 During the Maintenance Phase all changes to the system follow FRM-021-01 IT Change
Control Form l and SOP-008 Incident Management procedures and must be approved by
the System Owner and QA.
6.6.3 On a pre-determined frequency, IT and System Owner perform periodic reviews of system
requirements, validation, user access and audit trails/metadata.
6.6.3.1 Periodic reviews of systems are conducted as described in SOP-025 Periodic
Review of IT Systems and specific system’s validation plan (VP), as appropriate.
Reviews will include the following:
• Confirmation that the version of the software in use is the same as
documented
• Validation documentation is adequate to represent the actual system
• Review of change controls since the last periodic review
• System is being used per SOPs
• Review of system security including assessing that only the appropriate
users have access to the system
6.6.3.2 Periodic reviews of user access management, identification coder and passwords
are managed in accordance with SOP-019 User Acces Management.
6.6.3.3 Periodic reviews of system’s metadata including audit trails follow procedures
described in SOP-017 Audit Trail Review.
6.6.4 Deviations, deficiencies identified during periodic reviews must be documented, impact
assessment is conducted and as appropriate, managed through the procedures for
incident reporting per SOP-008 Incident Management, and/or corrective actions SOP-007
Corrective and Preventive Action (CAPA).
6.7 System Backup/Restore
6.7.1 GxP system backup and restore processes managed by external technical service
providers are maintained in accordance with service level agreement (SLA) between
Netramind and the service provider, and service provider’s procedures.
6.8 Disaster Recovery (DR)
6.8.1 GxP system disaster recovery processes managed by external technical service providers
are maintained in accordance with service level agreement (SLA) between Netramind and
the service provider, and service provider’s procedures.
6.8.2 DR testing and assessment of Netramind GxP systems are handled in accordance with
SOP-023 IT Disaster Recovery.
6.9 Business Continuity (BC)
6.9.1 BC testing and assessment of Netramind GxP systems are handled in accordance with
SOP-025 Business Continuity.
6.9.2 In case of unavailability of the system(s) for extended period, Netramind may delegate or
outsource GxP activities to service providers as necessary.
6.10System Decommissioning
6.10.1 When it is determined that a system is to be obsoleted, replaced or upgraded, the action
of retiring the system must be initiated through change control and adhere to procedures
described in SOP-010 Software Development Lifecycle.
6.10.2 All validation documentation will be filed and retained until all data associated with the
system has been destroyed in accordance with regulations.
6.11Documentation
6.11.1 Review documentation to determine which documents have been impacted by a change.
All approved documents that have been affected should be updated in accordance with
the SOP Configuration Management.
6.11.2 Verify all supporting documents have been updated to reflect the changes.
6.11.3 Maintain all supporting documents and have accessible for reference during
maintenance.
7 ATTACHMENTS
• FRM-021-01 IT Change Control Form
• FRM-021-02 Incident Request Form.
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
