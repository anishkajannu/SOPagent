# SOP-022 — IT Network Management

1 PURPOSE
This Standard Operating Procedure (SOP) defines the administration process for network devices and
resources that manages connectivity for the Netramind secure network.
2 SCOPE
This procedure applies to network and connectivity resources managed by Netramind in support of
GxP-regulated activities, including cloud-hosted environments, remote access technologies, firewalls,
wireless networks, and related infrastructure components where applicable.
3 REFERENCES
• SOP-012 IT Change Control
4 DEFINITIONS
4.1 Active Directory (AD)—Active Directory (AD) is a Microsoft product that consists of
several services that run on Windows Server to manage permissions and access to
networked resources. Active Directory stores data as objects. An object is a single
element, such as a user, group, application, or device, such as a printer.
4.2 Extension Virtual Network Resources—Externally hosted network resources (i.e.,
Amazon Web Services, Google Cloud, Microsoft Azure, etc.) that are configured and
controlled by Netramind Network Administrators as an extension of the Netramind
Secure Network.
4.3 Incident—An unplanned interruption to an IT service or reduction in the quality of an IT
service or a failure of a component item that has not yet impacted an IT service.
4.4 Local Accounts—Privileged accounts local to the device, that are used in cases where
connectivity to AD is not available.
4.5 NETADMIN– Network Administrator
4.6 Privileged Accounts—Accounts with elevated rights to key information assets including,
but not limited to, operating systems, database server, user directories, network devices
and enterprise resource planning application. Privileged users of these accounts include,
but are not limited to, system, database, and network administrators, IT Service Desk, and
application owners.
5 RESPONSIBILITIES
5.1 Network Administrators (NETADMIN) or Designee
5.1.1 Supporting the Netramind network environment by ensuring that network devices
are managed, monitored, and maintained for their intended use.
5.1.2 Configuring and Monitoring extension virtual network resources for use by
Netramind personnel.
5.2 Security Subject Matter Expert (SME) or Designee
5.2.1 Reviewing significant security findings where applicable.
5.3 System Owner (SO) or Designee
5.3.1 Reviewing and approving updates to the Netramind network configuration.
5.3.2 Approving network privileged account requests.
5.3.3 Approving all change requests.
5.4 Quality Assurance (QA) or Designee
5.4.1 Approving change requests that affect GxP Computerized Systems.
6 PROCEDURE
6.1 Account Maintenance
Local Stored in
Privileged
Network Resource Privileged 1Passwor
AD Account
Account d Vault
On-Premise Firewalls Yes Yes No
On Premise Physical Network Devices (Other) Yes Yes Yes
Extension Virtual Network Resources Yes Yes* Yes*
*Note: Only local privileged accounts are stored in the password vault. Passwords that are
linked to a named Netramind Active Directory user account are handled through Active
Directory and not stored in 1Password vault.
6.1.1 Authorized NETSADMIN shall login to network resources using the appropriate
active directory credentials, whenever possible. For devices that do not support
active directory authentication, the local privileged account can be used.
6.1.2 Privileged account passwords are managed according to Netramind security
practices.
6.1.3 Local Account credentials are managed in an appropriate cloud application. Local
Account credentials are securely managed and periodically reviewed.
6.1.4 Privileged account access is periodically reviewed by appropriate personnel.
6.2 New network resource Deployment
6.2.1 Significant network changes are managed through the applicable change control
process.
6.3 Patching and Upgrades
6.3.1 Upgrades to network resources will follow the appropriate change control process
and will be performed by NETADMIN as needed.
6.4 Monitoring
6.4.1 Network resources and security-related events may be monitored using appropriate
infrastructure and security tools where applicable.
6.5 Documentation
6.5.1 Relevant network documentation is maintained in controlled repositories with
appropriate access restrictions.
6.6 Change Management
6.6.1 Changes to network resources will be managed in accordance with IT Change
Management (Non-GxP).
6.6.2 The change control record will identify the appropriate updates to system
documentation (i.e., network design diagrams, network routing, device
configuration, asset inventory, etc.).
6.7 Incident Management
6.7.1 Network-related incidents are documented and managed through the applicable
incident management process.
6.7.2 For events that affect GxP computerized systems, NETADMIN/SO will evaluate
each reported incident, consult with QA on the GxP relevance, and document their
resolution in a deviation, CAPA, or Change Control if applicable.
6.8 Backup/Recovery
6.8.1 Backup
6.8.1.1 Configuration backups for critical network resources may be maintained
where appropriate to support recovery and restoration activities.
6.8.2 Restoration
6.8.2.1 Network configurations may be restored from available backup or
configuration management records where applicable.
6.9 Security
6.9.1 Physical Security
6.9.1.1 Physical access to network infrastructure is restricted where applicable.
6.9.2 Logical Security
6.9.2.1 All network resources will require authentication of a privileged account
by a NETADMIN for viewing and management.
6.9.3 Network Penetration Testing
6.9.3.1 Security assessments or vulnerability reviews may be performed
periodically based on system risk, infrastructure complexity, and business
needs.
6.10Firewall rules management
6.10.1Firewall and network security configurations are reviewed and updated as
appropriate to support secure operations and business requirements.
7 ATTACHMENTS
N/A
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
