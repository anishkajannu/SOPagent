# MAN-018-02 — Heidelberg SD-OCT Image Acquisition and File Export Manual - OCU410-301

Heidelberg SD-OCT Image Acquisition and File Export Manual
Protocol: OCU410-301
UNCONTROLLED COPY IF PRINTED
Contents
1. Study-Specific OCT Requirements ............................................................................................................................... 3
2. Instrumentation and Software Requirements ............................................................................................................ 4
2.1 System Requirements ........................................................................................................................................ 4
2.2 Alternate Heidelberg Spectralis Instrumentation and Software ..................................................................... 4
2.3 Ability to Transfer Files Off of OCT System ....................................................................................................... 4
3. Summary Procedures ................................................................................................................................................... 5
4. Create a NORC Exports Folder on Your Desktop for Scan Exports ............................................................................. 6
5. Check / Configure Heidelberg Spectralis Software ..................................................................................................... 6
5.1 Check the Heidelberg SD-OCT Software Versions ................................................................................................. 6
5.2 Change the Destination Folder for Raw Data Exports to the “NORC Exports” Folder ........................................ 9
6. Creating and locating a study patient in the Heidelberg SD-OCT system ................................................................ 11
6.1 Procedure for Creating the Study Patient Identity.............................................................................................. 11
7. SCAN ACQUISITION PROCEDURES ............................................................................................................................. 18
8. Export Procedures ...................................................................................................................................................... 23
9. NORC File Transmission Instructions ......................................................................................................................... 27
9.1 System Requirements .......................................................................................................................................... 27
9.2 NORC File Transfer Accounts ............................................................................................................................... 27
9.3 Image Transmission Description .......................................................................................................................... 27
9.4 Using the NORC File Transfer Portal .................................................................................................................... 28
9.5 Submission Follow-Up ..................................................................................................................................... 28
10. Revision History ........................................................................................................................................................ 29
11. Signature Page .......................................................................................................................................................... 30
Appendix A ..................................................................................................................................................................... 31
A. Purpose....................................................................................................................................................................... 31
B. Definitions and Grading Criteria ................................................................................................................................ 31
UNCONTROLLED COPY IF PRINTED
1. Study-Specific OCT Requirements
This section details the instrument-specific (i.e., Heidelberg Spectralis HRA + OCT) OCT requirements for
the OCU410-301 Study.
Eyes to be Studied: Both eyes (OU)
Requirement Macular Volume Scan ONH Scan
Eyes Both eyes (OU) Both eyes (OU)
Imaging Mode IR + OCT —
Scan Pattern Volume Scan (20° × 20°) ONH Scan (15° × 15°)
B-Scan Sections 97 37
OCT ART Mean 9 frames (minimum) 9 frames (minimum)
Scan Quality ≥ 20 ≥ 20
Field of View 30° Mode 30° Mode
OCT Volume Resolution High Speed High Speed
Required Images (OU):
● IR+OCT
● Separate IR (Field 2)
● Separate autofluorescence images (Field 2)
File Format and Submission:
Export Heidelberg E2E files via the NORC secure file transfer portal as the primary method for submitting
imaging data, or CD/DVD/External drive if needed (see Section 10).
Required OCT Equipment and Software:
● Instrument: *Heidelberg Spectralis HRA + OCT
● HRA2 / Spectralis Family Acquisition Module Version: 4.0.0.0 or higher
● HRA / Spectralis Viewing Module Version: 4.0.0.0 or higher
● Heidelberg Eye Explorer (HEYEX) Version: 1.6.1.0 or higher
*See Section 2-B for alternate Heidelberg SD-OCT instrumentation and software.
UNCONTROLLED COPY IF PRINTED
2. Instrumentation and Software Requirements
Please read this section carefully and contact NORC if you have any questions.
2.1 System Requirements
Acceptable instrumentation for this protocol is the Heidelberg Spectralis HRA + OCT, with HRA2 /
Spectralis Family Acquisition Module Version 4.0.0.0 or higher, HRA / Spectralis Viewing Module Version
4.0.0.0 or higher, and Heidelberg Eye Explorer (HEYEX) Version 1.6.1.0 or higher.
Please note: This protocol has been written for the above-mentioned instrument and software versions.
However, other instruments and software versions will also be accepted. These are listed in Section 2-B,
below. Please keep in mind that some of the screen captures and procedure steps presented in this manual
may be different for the different instruments listed in Section 2-B.
2.2 Alternate Heidelberg Spectralis Instrumentation and Software
Instrument: Heidelberg Spectralis OCT
Software Version: 5.0 or higher; Spectralis Family Acquisition Module Version: 5.0.2.0 or higher;
Heidelberg Eye Explorer (HEYEX) Version: 1.6.1.0 or higher
Instrument: Heidelberg Spectralis OCT Plus
Software Version: 4.0 or higher; Spectralis Family Acquisition Module Version: 4.0.0.0 or higher;
Heidelberg Eye Explorer (HEYEX) Version: 1.6.1.0 or higher
Instrument: Heidelberg Spectralis FA + OCT
Software Version: 4.0 or higher; Spectralis Family Acquisition Module Version: 4.0.0.0 or higher;
Heidelberg Eye Explorer (HEYEX) Version: 1.6.1.0 or higher
(If you do not have updated software, please contact your Heidelberg Spectralis representative to request
a software upgrade.)
2.3 Ability to Transfer Files Off of OCT System
Your system must have the capability to transfer digital files off the Heidelberg SD-OCT computer so that
they can be transmitted to NORC via the online portal. The easiest way to do this may be to connect a
USB device such as a flash drive to the Heidelberg SD-OCT machine, the contents of which can be sent
directly to NORC or transferred to another computer to be uploaded via web-transmission to NORC.
Please be sure that you have the above hardware and software capabilities before beginning study
activities.
UNCONTROLLED COPY IF PRINTED
3. Summary Procedures
This section summarizes the study-specific SD-OCT procedures for the actual patient visit. Images for
qualification should also follow these procedures.
● Create an export location (Section 4) – Note: this only needs to be done once.
● Check / configure Heidelberg SD-OCT software (Section 5)
● Check / configure Windows Explorer (Section 6)
● Create, or locate the study patient in the Heidelberg SD-OCT database (Section 7). If available,
USE HEYEX FOLLOW-UP FUNCTION
● See Section 8 for Scan Acquisition settings.
● Scan the Patient (Section 8).
● Verify that scan quality is ≥ 20. The Scan Quality factor will be displayed on the screen. Rescan if
needed to acquire a good quality scan (Section 8).
● Save the scan (Section 8).
● Export the data files for a single patient visit to the “NORC Exports” folder (Section 9).
● Upload via the NORC secure file transfer portal (Section 10), or CD/DVD/USB/HARD DRIVE.
Scans to Acquire
For both site qualification and study subject imaging, acquire the required Macular Volume and ONH
scans for both eyes (OU) using the study-specific scan parameters listed in Section 1.
UNCONTROLLED COPY IF PRINTED
4. Create a NORC Exports Folder on Your Desktop for Scan Exports
This section gives procedures for creating a folder on your desktop into which you will export the NORC
study scans. This procedure only needs to be done once to set up your system.
Start from your Windows Desktop. Right-click on the desktop and select New Folder. When the new
folder icon appears, type “NORC Exports (Figure 1).”
Figure 1. Create a “NORC Exports” folder on the Desktop.
5. Check / Configure Heidelberg Spectralis Software
This section explains how to:
● Ensure that the Heidelberg Eye Explorer (HEYEX) Version is 1.6.1.0 or higher.
● Ensure that the HRA2 / Spectralis Family Acquisition Module Version is 4.0.0.0 or higher.
● Ensure that the HRA / Spectralis Viewing Module Version is 4.0.0.0 or higher.
● Change the destination folder for Raw Data Exports to the “NORC Exports” folder.
Note: See Section 2.2 for alternate hardware and software versions.
5.1 Check the Heidelberg SD-OCT Software Versions
1. Double-click on the Heidelberg Eye Explorer Icon.
2. When the Main Screen opens, select Help - About from the Main Menu (Figure 2).
UNCONTROLLED COPY IF PRINTED
Figure 2. Access “About Heidelberg Eye Explorer” Information.
3. The “About Heidelberg Eye Explorer” box will be displayed, showing the Version of Heidelberg
Eye Explorer, the Version of HRA2 / Spectralis Family Acquisition Module, and the Version of HRA
/ Spectralis Viewing Module (Figure 3).
UNCONTROLLED COPY IF PRINTED
Figure 3. Software Versions.4. If the version of Heidelberg Eye Explorer is not 1.6.1.0 or higher,
the version of HRA2 / Spectralis Family Acquisition Module is not 4.0.0.0 or higher and/or the
version of HRA / Spectralis Viewing Module is not 4.0.0.0 or higher, please contact your
Heidelberg representative for a software upgrade.
UNCONTROLLED COPY IF PRINTED
5.2 Change the Destination Folder for Raw Data Exports to the “NORC Exports” Folder
5.2.1 Launch the Heidelberg Eye Explorer software by double-clicking on the software icon.
5.2.2 When the Main Screen opens, click on Setup - Options from the Main Menu (see
Figure 4).
Figure 4. Setup “NORC Exports” Folder for Scan Exports
5.2.3 When the “Options” box opens, click the “Plug Ins” tab, select “hraviewer” in the
selection window, and click Setup (see Figure 5).
UNCONTROLLED COPY IF PRINTED
Figure 5. “hra viewer” Highlighted in Selection Window on “Plug Ins” Tab
5.2.4 When the “Preferences” box opens, click “Raw DataExport Options” in the “Preferences”
(selection) window (see Figure 6). The Raw Data Export Options view will be displayed.
UNCONTROLLED COPY IF PRINTED
Figure 6. “Raw Data Export Options”
5.2.5 On the “Preferences” box, browse to the “NORC Exports” destination folder in the
“Destination folder for export files” section, leave the “post-processing application” field blank,
and select Graphics file format as E2E (Figure 7).
Figure 7. “Preferences” Box
6. Creating and locating a study patient in the Heidelberg SD-OCT
system
These procedures describe how to create a new study patient in the Spectralis HRA +
OCT system, and to locate a study patient that has already been created.
The first time you perform imaging on a new study patient, you will create the study patient
using the identity masking procedures provided in this section.
6.1 Procedure for Creating the Study Patient Identity
6.1.1 Launch the Spectralis HRA + OCT software program by double- clicking on the
Heidelberg Eye Explorer icon . The “Main Screen / Database Window” will
UNCONTROLLED COPY IF PRINTED
open (see Figure 8). See Figure 9 for shortcut buttons.
Figure 8. Main Screen / Database Window
UNCONTROLLED COPY IF PRINTED
Figure 9. Shortcut buttons
6.1.2 On the “Main Screen / Database Window”, click on the “New Patient” icon (Figure 10).
Figure 10. New Patient Icon
6.1.3 When the “Patient Data” box opens, enter the study patient’s data as listed
below, depending on whether you are submitting a study patient visit (Figure
11), or qualification images.
UNCONTROLLED COPY IF PRINTED
For study patients-
Complete the patient demographic fields according to the Sponsor
Guidelines. Unless otherwise instructed by the sponsor, leave all
remaining fields blank.
Figure 11. Patient Data Box
6.1.4 Click OK (see Figure 11. The “Examination Data” box will open (Figure 12).
UNCONTROLLED COPY IF PRINTED
Figure 12. “Examination Data” box
6.1.5 On the Examination Data box, select “Spectralis HRA + OCT” from the “Device type”
drop-down menu (if you are using an instrument other than the Spectralis HRA + OCT,
select the appropriate device type, corresponding to your specific instrument). Select
your initials from the “Operator” drop-down menu (if your initials are not available in
the drop-down menu, type in your initials, and it will get saved in the drop-down menu
automatically). Leave the “Study” field blank. Click OK See Figure 12, above.
6.1.6 The “Eye Data” Box will open (Figure 13).
Figure 13. “Eye Data” box
UNCONTROLLED COPY IF PRINTED
6.1.7 DO NOT enter/change any data in the “Eye Data” Box. (Leave all default settings in
all the fields, as is / unchanged.) See Figure 13, above. Click OK
6.1.8 A preliminary Image Acquisition window will be displayed (Figure 14). If you are
ready to scan the patient for the Baseline visit, go ahead to section 6B. (Now that you
have set up the patient in the database, you also have the option of scanning the
patient at a later time by calling up the patient by performing a patient-search.)
Figure 14. Preliminary Image Acquisition Screen
6.2 Locate the Patient for Scanning
You should have already set up the patient in the Heidelberg SD OCT Database
6.2.1 From the main screen, perform a patient-search by typing the sponsor (and protocol,
if needed) in the “Name” field and clicking Update Display (see Figure 15)
UNCONTROLLED COPY IF PRINTED
Figure 15. Patient-search
6.2.2 When the study patient is displayed, select the patient and click on the “New
Examination” icon (see Figure 16).
Figure 16. Highlight Patient and click “New Examination”
6.2.3 When the “Continue Examination” Box opens, click Yes
(See Figure 17).
Figure 17. Confirm Patient Re-examination
UNCONTROLLED COPY IF PRINTED
7. SCAN ACQUISITION PROCEDURES
• After the preliminary Image Acquisition window opens (Figure 14), the Laser On/ Off
button on the Control Panel will automatically turn from red to yellow.
• Perform the following steps on the Control panel:
(Note: Control Panel display colors; inactive / unselected buttons will display in Red,
and active / selected buttons will display in blue.)
i) Press the Yellow On / Off button on the Control Panel to activate the laser and camera.
The screen will change as shown in Figure 22, and the Acquisition Menu will be
displayed on the Control Panel (see Figure 19).
Figure 18. Screen after Laser and Camera are Activated
UNCONTROLLED COPY IF PRINTED
Figure 19. Control Panel
ii) Make sure that the “OCT” button is selected (displayed in blue). If not, select it. See
Figure 19.
iii) Select the IR + OCT button (display it in blue). See Figure19.
iv) Make sure that the “Volume” button is selected (displayed in blue). If not, select it. See
Figure 19.
v) Make sure that the Field of View is 30° (displayed in blue). If not, select it. See
Figure 19.
vi) Select the appropriate IR laser intensity to adjust for patient media (Typically, 50 –
75%). The default setting is 100%. See Figure 19.
vii) If the Resolution setting on your Control Panel does not default to “High Res.”,
select the “More” button on the Acquisition Menu, and when the Resolution Mode
menu is displayed, select “High Speed.” (see Figure 20). Click on the back arrow to
go back to the Acquisition menu.
UNCONTROLLED COPY IF PRINTED
a.
b. Figure 20. Resolution Mode – High Speed.
viii) Press the Sensitivity / ART button located below the touch pad of the Control
Panel (see Figure 21). The screen will change as shown in Figure 22, with the
addition of a small ART (Automatic Real Time) image window at the bottom of the
screen.
Figure 21. Sensitivity / ART Button
UNCONTROLLED COPY IF PRINTED
Figure 22. Screen with a small ART Image Window at bottom of Screen
• Bring the camera and patient into position, adjust alignment, distance, and focus to optimize
image quality.
• Utilize the OCT Acquisition window on the monitor to align the camera with the
Fundus image on the left side of the screen. A cross-sectional image of the retina will
appear in the OCT image window (see Figure 23).
• Focus the IR photograph on the blood vessels and ensure that the OCT image on the
right side of the screen is no lower than in the center of the OCT image window
• Select / check the following settings on the OCT Acquisition window:
i) Scan Pattern: check that Volume Scan (20° x 20°) is displayed.
ii) Number of Sections in the scan pattern: the number of sections defaults to 19. Increase
the sections to 97 by pressing the Shift key + the Up (↑) Arrow key on the keyboard until
97 sections is reached. If it is too difficult to acquire these many scans because the
patient is poor fixator and scan time is too long, it is okay to reduce to 49 B-scans (please
inform the situation to NORC).
iii) OCT ART Mean: ensure that an OCT ART Mean of 15 frames is selected and
UNCONTROLLED COPY IF PRINTED
displayed (to increase or decrease the number of frames, move the bar under
OCT ART Mean to the right or left respectively). If you have difficulty with
capturing at an ART of 15 (e.g., patient is a poor fixator and scan time is too
long, it is okay to reduce the ART, though ART levels below 9 may reduce the
quality of our grading.
iv) Scan Quality: ensure that a Scan Quality Factor of ≥ 20 is reached.
v) Eye Length: select “M” (medium). If focus cannot be obtained at this setting, adjust the
default Eye Length of Medium to “S” (short), “L” (long), or “XL” (extra-long) until the retina
is focused.
vi) Eye (OD/OS): the Eye will automatically be selected depending on the position of the
camera. Therefore, no selection is required as to OD or OS.
vii) Field of View: check that the Angle is at 30° (this selection was made on the Control
Panel).
viii) Mode: Check that Mode is OCT Volume.
ix) Resolution: check that “Res.” Is “High Speed.”.
• When all the required scan parameters are selected and/or optimized, press ACQUIRE on the
Control Panel.
• After the scan is complete, if the visit requires both eyes to be scanned, move the camera
backwards and over, to focus on the opposite eye, and acquire the scan of the opposite eye
by following Steps 3 – 7 above. (Note: You will be aware that the scan is complete, when the
small OCT ART Image window disappears from the bottom of the screen, and the B-scans
have migrated from the bottom to the top of the IR image).
• Click “Save” on the upper left side of the screen (see Figure 23) on the Menu Bar to save the
OCT scan/s. NOTE: Scans of both eyes can be saved at the same time.
• Click “Exit” on the upper left side of the screen on the Menu Bar to exit the OCT Image
Acquisition screen.
• Proceed to the next section (8) for export procedures.
UNCONTROLLED COPY IF PRINTED
8. Export Procedures
Export all Spectralis data (OCT, IR and FAF images for each eye or each subject) in .E2E format.
1. To begin exporting the scan in .E2E format, right-click on the icon representing the scan that
needs to be exported. The options list-box with the Export functionality enabled will be displayed.
Hover over “Export," and a subsidiary options list-box with export file formats will be displayed. Click
on an E2E, then repeat steps to complete the export.
2. After the export of .E2E has been completed, using Windows Explorer, locate and double-click on
the “NORC Exports” folder to open it. From the Windows menu, select View - Thumbnails. You
should see, for a single eye, one .E2E file for each eye or each imaging scan (all images, macular
volume scan, ONH scan, IR images and FAF images of each subject (2 eyes) can be exported in a
single .E2E file).
HRA2 OCT Volume Data Exporting Procedure
Before You Begin
 Confirm the subject's OCT volume(s) have been fully acquired and saved in HEYEX before starting
the export process.
 Have the subject's Subject ID and Visit Number available for the naming step.
 Confirm the study-specific data folder has already been created on the desktop.
Step 1 Select the OCT Volume
Select the OCT volume(s) to be exported, as indicated by the white box in the HEYEX interface.
UNCONTROLLED COPY IF PRINTED
Step 2 Export the OCT Volume
In the Export tab on the right side of the HEYEX window, drag and drop the selected OCT volume(s) into
the "E2E Anonymized & Rename Drive."
Step 3 Rename the Exported Data
Double-click "E2E Anonymized & Rename Drive." This will allow you to rename the exported E2E
volume according to the study-specific naming instructions.
UNCONTROLLED COPY IF PRINTED
Step 4 Apply the Study-Specific Naming Convention
The photographer should rename the exported E2E volume according to the study naming convention
recommended by the sponsor.
Step 5 Transfer the Renamed Data to the Study Folder
After renaming the E2E volume, drag and drop the data from the “E2E Anonymized & Rename Drive” to
the pre-created study data folder on the desktop.
To do this, drag the data to the appropriate drive shown under Output Devices (e.g., C:\). A Browse for
Folder window will then appear. Select the appropriate study folder on the desktop and click "OK" to
transfer the subject's data.
UNCONTROLLED COPY IF PRINTED
Step 6 Confirm Data Transfer
After clicking "OK," a status bar will appear indicating the progress of the data transfer from HEYEX to
the selected study folder.
Wait until the transfer is complete and verify that the data have been successfully transferred to the
appropriate folder.
Example folder name: SubjectID_VisitNumber_OD
Step 7 Upload the Data to the NORC Portal
After completing the export and transfer process, upload the entire folder containing all E2E files for the
corresponding subject and visit to the NORC Portal, following the study-specific upload instructions.
Important: Please ensure that all E2E files associated with the same subject/visit are included in the
folder before uploading.
UNCONTROLLED COPY IF PRINTED
Questions or Issues:
If you encounter any issues exporting, renaming, or uploading OCT volume data, please contact the
NORC Reading Center before proceeding.
9. NORC File Transmission Instructions
9.1 System Requirements
● A computer running a supported Windows Operating System. If your browser has issues during
uploading, re-attempt using another web browser (e.g., Firefox, Chrome, etc.)
● Contact NORC before attempting to upload files, and instructions/access details will be
provided.
9.2 NORC File Transfer Accounts
If you already have login credentials for the NORC secure file transfer portal, continue to use
your current account. Contact NORC if you have forgotten your username or password or are
unsure whether you have an account.
If you do not already have an account, contact NORC (see contact information below) regarding
account creation. In the e-mail, include the following information:
● Name of the study
● Name of your principal investigator
● Name of Institution/site
● Address of Institution/site
● Site #
● Account holder’s name
● Account holder’s phone number
● Account holder’s e-mail address
After your request is processed, you will receive email confirmation of account access and login
details. If you do not receive these within a few business days, contact NORC.
9.3 Image Transmission Description
Please ensure that any digital images and digital file names are devoid of actual patient
information such as name, DOB and medical record number. NORC cannot receive any
protected health information (PHI) as defined in the HIPAA regulations.
UNCONTROLLED COPY IF PRINTED
9.4 Using the NORC File Transfer Portal
i) Log in to the NORC secure file transfer portal at the URL provided by NORC.
ii) Click the “Folders” link.
iii) Upload the files by dragging and dropping or clicking upload files then drag and drop.
iv) Confirm all files were uploaded as larger files may take some time.
v) When NORC receives your upload, the images will be downloaded for review.
vi) If you suspect a problem with the submission, or you wish to submit replacement images for
any reason, contact NORC for instructions.
9.5 Submission Follow-Up
The NORC Site Portal is the primary method for submitting imaging data. A separate email
notification is not required for routine submissions.
For expedited review or follow-up regarding a submitted qualification or study visit, sites may
contact NORC at norc@netramind.ai or submit the request directly through the NORC Site Portal.
Refer to the NORC Portal User Guide for instructions.
To assist NORC in identifying and reviewing the submission, include the following information, as
applicable:
● Protocol: OCU410-301
● Site number
● Qualification or Study Visit
● Subject ID and visit, if applicable
● Submission date
● Reason for follow-up or expedited review
UNCONTROLLED COPY IF PRINTED
10. Revision History
Version Number Date Summary of Change(s)
01 13-AUG-2026 New Document
UNCONTROLLED COPY IF PRINTED
11. Signature Page
Author:
DATE DD-MMM-
NAME TITLE SIGNATURE
YYYY
Sandeep Chandra
Director of AI
Bollepalli
QA:
NAME TITLE SIGNATURE DATE
Jay Chhablani President
Approver:
NAME TITLE SIGNATURE DATE
Justin Shaka Fractional COO
UNCONTROLLED COPY IF PRINTED
Appendix A
OCT Image Quality: Acceptable vs. Unacceptable Images
Grading Reference for Reading Center Certified Graders
A. Purpose
Image quality is determined by the ability to assess features for each study variable. In general, the
more noise or distortion present in an image, the lower the resulting image quality grade. Here are
general guidelines for overall quality of the images. Details analysis of the quality will be done by our
reading center and acceptance or rejection for biomarker-specific quality for the whole volume will be
informed 24-48 hours after uploading the images.
Retake scans if you notice any of the following:
• A “noisy” background (numerous white dots in the aqueous space — the dark area at the top of
the image — resembling snow)
• Breaks or discontinuities along the horizontal scan due to image artifact
• A non-centered fovea,
• Image tilting
• Other artifacts described below
B. Definitions and Grading Criteria
B.1 Adequate
Adequate implies that photographic features can be read with great confidence.
 Retinal layers (ILM through RPE/Bruch’s membrane) are clearly delineated across the entire scan
 Background (aqueous space) is dark and free of significant noise
 Fovea is well-centered, with the characteristic foveal depression clearly visible
 No significant motion artifact or misalignment between B-scans
 Signal strength meets or exceeds the device-specific acceptable threshold
 All landmarks required for study-variable grading (e.g., RPE, ELM, EZ, ONL/OPL) are
distinguishable
UNCONTROLLED COPY IF PRINTED
Example: Adequate image quality
B.2 Fair
Fair implies that all or nearly all photographic features can be read, but confidence in grading is only fair.
 Most retinal layers are identifiable, though borders may be slightly indistinct in localized areas
 Mild-to-moderate background noise is present but does not obscure key landmarks
 Fovea is reasonably centered; slight tilt or decentration does not prevent grading
 Occasional artifact (e.g., blink line, minor motion) is present but does not affect critical grading
regions
 Primary study variables remain assessable despite reduced grading confidence
Example: Fair image quality
B.3 Poor
Poor implies that photographic features cannot be read with great confidence due to poor image
quality; therefore, some or all features may not be gradable.
 Significant noise or speckle obscures the boundaries of one or more retinal layers
UNCONTROLLED COPY IF PRINTED
 Layer boundaries are blurred, discontinuous, or difficult to distinguish in critical regions
 Fovea is poorly centered or tilted, limiting assessment of foveal-involving features
 Visible motion artifact, banding, or horizontal discontinuity is present across the scan
 One or more study variables may not be gradable; retake is recommended if feasible
Example: Poor image quality
B.4 Cannot Grade (CG)
Cannot Grade (CG) implies that photographic features essential for grading cannot be reliably assessed
due to severe image-quality issues, artifacts, or missing image data. A scan should be classified as CG if
any of the scenarios below are present:
 Movement artifact severe enough to distort, duplicate, or discontinue the retinal contour
 Signal strength/image quality too low to distinguish any retinal layers
 Missing portion(s) of the scan or volume (cropped field, incomplete B-scans)
 Misalignment or missing segments within the volume scan that prevent reliable measurement
 No usable landmarks remain for grading any study variable
Common CG Scenarios:
OCT image with movement artifact
UNCONTROLLED COPY IF PRINTED
Movement artifact distorting the retinal contour
Poor image quality to grade study variables
Signal too low to reliably distinguish retinal layers
Missing part of scan/images
Cropped field with missing scan data
Misaligned/missing portion of the volume scans
UNCONTROLLED COPY IF PRINTED
Misalignment between fundus reference and OCT volume
UNCONTROLLED COPY IF PRINTED
