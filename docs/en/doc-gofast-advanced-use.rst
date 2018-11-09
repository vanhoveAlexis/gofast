GoFAST: Advanced Use
====================

Introduction
------------
The document is intended to provide instructions for configuring third-party software
that runs with the GoFAST platform.

The complementary tools allow having:

* Mobile working :

 * Working in "disconnected" mode (DropBox type)
 * Access to GoFAST on mobile devices (tablets, ...) with File Explorer
 * Displaying and / or online editing Office documents on your tablet
 * Instant messaging ("chat") on mobile phone
 * Videoconferencing on the mobile phone (in browser)

* Scanning  tools (smartphone, copier, ...)

* Signature tools
 
 
Local synchronization (GoFAST offline)
--------------------------------------

CMISSync is a powerful and reliable tool that allows having synchronization
on a PC of one or more collaborative spaces of GoFAST.

If you do not have network access (for example in the plane), the GoFAST files are
available on your computer's hard drive and you can still work with them.

If you change them they will be directly synchronized as soon as the network is available.

CMISSync installation
^^^^^^^^^^^^^^^^^^^^^
The tool is available for Windows, Mac (beta) and Linux and can be downloaded 
here: https://bitbucket.org/aegif/cmissync/downloads

The current recommended Windows version * is **2.9.4.0** or **2.11.3.0** (under test)

There are the steps to configure the tool (**myorg** is to be replaced by the name of your organization)

The address to use:
`https://gofast. <https://gofast.myorg.com/alfresco/api/-default-/public/cmis/versions/1.1/atom>`__\ `**myorg** <https://gofast.myorg.com/alfresco/api/-default-/public/cmis/versions/1.1/atom>`__\ `.com/alfresco/api/-default-/public/cmis/versions/1.1/atom <https://gofast.myorg.com/alfresco/api/-default-/public/cmis/versions/1.1/atom>`__

|image3|

At this stage, it is possible to choose the collaborative space that you want to synchronize.
Of course if this collaborative space contains subspaces they will be synchronized and
therefore the data volume at the first synchronization can be very important.
Expect for example 30 minutes of synchronization for 1700 files / 1.2 GB.

If you want to synchronize everything, choose the "root" space, 
here "Main Repository"

|image4|

Once configured it is possible to do several actions such as open the local synchronization folder,
pause the synchronization or change the settings.

|image5|


.. IMPORTANT:: In the settings it is possible to reduce the synchronization frequency, it is a useful option if CMISSync 
               is widely distributed in the organization because CMISSync can load the GoFAST platform. More precisely, 
               CMISSync consumes bandwidth on server side and CPU.
               
|image6|        


Use
^^^
When the computer is connected to the network, CMISSync periodically checks
whether documents have been changed on the GoFAST platform.
If the documents have been changed, they are copied locally (on your PC).


.. NOTE:: If you make changes offline, when there is a reconnection to the GoFAST server,
          your version will be uploaded and versioned unless a user has made changes to
          the GoFAST in the meantime. In this case a "conflict management" is activated.
          See below.
          
          
          
Example of notification (English version)

1) User A and User B have the synchronized file **mail.doc** on their desktop.

2) User A and User B disconnect (offline), and each of them edits **mail.doc** locally.

3) User A becomes connected again (online). CMISSync uploads the **mail.doc** version of User A
to the GoFAST server (which creates a new version automatically).

4) User B becomes connected again. CmisSync tries to upload the User B version of **mail.doc**
to the GoFAST server, but finds out that the file has already been modified by User A.

5) On the User B PC, CmisSync renames User B version of **mail.doc** in mail.doc_User B-version
and download **mail.doc** of User A on the PC. 

6) Now User B has 2 versions, and must do one of 3 actions:

a. Keep the version of User A: Delete the **mail.doc_UserB-version**

b. Keep the version of User B: Delete **mail.doc** (UserA) and remove the suffix
of the **mail.doc_UserB-version**. In this case the version of B will be overwritten
on the GoFAST server after versioning.

c. Combine 2 versions in **mail.doc**, and after that delete **mail.doc_UserB-version**.

.. Danger:: As a precaution, it is better to avoid deleting a local directory in the synchronized tree.
            If you do that, the remote directories will be deleted. 
            GoFAST does not delete the documents permanently but
            the procedure of "republishing" must be done.


Access to GoFAST files on tablet and smartphone
----------------------------------------------------
The GoFAST platform can be accessed from Android tablets (eg GalaxyTab),
iOS (iPAD) and smartphones (Android, iOS, Blackberry).

For the access you need to install the free software **"Webdav Navigator Lite"** from  iTunes, GooglePlay
or Blackberry AppWorld. Please note that a paid version including local synchronization
is available under the name **"Webdav Navigator"**


|image9|

After that you will be able to access your GoFAST files on your smartphone:

|image10|

The publisher's site is at the following address :
http://seanashton.net/webdav/



Editing Office Files on Tablet
---------------------------------------
Android tablet
^^^^^^^^^^^^^^^^
For this type of tablet we recommend to use the Office Suite
" **WPS Office** " (available on GooglePlay).

You will be able to configure a storage space directly on GoFAST by "Open / Add cloud storage"
then choose "Webdav" and enter the address "https://gofast.mycomp.com/alfresco/webdav" where
you must replace mycomp.com by the domain of your organization.

|image14|

The application will ask for your username and password on the GoFAST.



After that it is possible to open a document directly on the GoFAST.
Some fonts do not exist in Android, the layout may be different from the one on the PC.

Saving can also change the layout slightly.

.. Important:: While saving the document, first it is saved locally on the tablet.
               Once the application is closed (X), synchronization is done with GoFAST.


iPad tablet
^^^^^^^^^^^^^
If you want just to view Office documents, we also recommend " **WPS Office** ".

Nevertheless, there is currently a limitation on the iPad version to save a document
that has been opened on the GoFAST. It is necessary to go through all the storage space
which is not very practical. The editor is notified of this bug and a fix should be produced.

While waiting for this hotfix, you can use the " **Citrix ShareFile QuickEdit** " suite.

|image15|

|image16|

Instant messaging ("chat") on mobiles
---------------------------------------------
|image6|

With GoFAST you have a private and secure instant messenger,equivalent to
"WhatsApp" for your Organization, running on the open standard XMPP.

Thus you can use an application for your phone following this standard.
For example:

- Android: Xabber (free), Kandru (free), Conversations (paid), Astrachat

- iOS: Chatsecure, AstraChat
For setting up these chat applications just enter in the account management options :

**Login** : your_gofast_login @gofast-comm.xxxxx.yyy
where xxxxx.yyy is the domain of your organisation

PDF Electronic signature
------------------------

GoFAST allows you to open a PDF with Foxit Reader (or Acrobat), to apply a signature
and save the signed PDF directly on the GoFAST platform.

.. NOTE:: You must have installed "ITHitEditDocumentOpener"

Then you can select  "Edit online" in the menu. It will open the application installed on your PC
(Acrobat Reader, Foxit, ...) and then you can sign with a handwritten signature or electronic certificate
and save directly to GoFAST while creating a version.

|image17|

.. CAUTION:: If you use Acrobat Reader, the application must be closed before launching the online edition.

Scan to GoFAST
--------------

It is possible to create a folder allowing to deposit PDF "Images" and that they are transformed into Text PDF.
It is achieved by a character recognition (OCR) commercial software installed on the PC, "ABBYY Hot Folder" (ABBYY FineReader).
It allows you to scan invoices and convert them into an Text PDF for an easy search on GoFAST.

|image19|

|image20|


Scan from a smartphone
----------------------

For example, it is possible to scan expense reports directly from a smartphone and send them directly to GoFAST.

|image18|

For that you must have installed:

-  CamScanner and "Webdav Navigator" or
-  Scanbot

We will discuss here the configuration of Scanbot which is more user-friendly.

|image11|

|image12|

|image13|

Scan from a multi-function copier
---------------------------------

In this case your copier must have a webdavs connector. Contact us for more details.


Content migration to GoFAST
---------------------------

GoogleDocs content migration/ Drive
^^^^^^^^^^^^^

In the case of migration from a Google repository to GoFAST, follow the procedure below:

.. image:: media-guide/GoogleDrive_Download_Export.png

Google offers to download a zip archive with content converted to MS-Office.

.. image:: media-guide/GoogleDrive_Download_Export_Step2.png

Now you can unpack the archive directly into the directory tree on GoFAST.

.. image:: media-guide/GoogleDrive_Download_Export_Step3.png


.. |image0| image:: img/mobilite/wps7DA7.tmp.jpg
.. |image1| image:: img/mobilite/wps7DB8.tmp.jpg
.. |image2| image:: img/mobilite/wps7DB9.tmp.jpg
.. |image3| image:: img/clip_image007.png
.. |image4| image:: img/clip_image009.png
.. |image5| image:: img/clip_image011.png
.. |image6| image:: img/clip_image034.png
.. |image7| image:: img/mobilite/wps7DBE.tmp.jpg
.. |image8| image:: img/clip_image017.png
.. |image9| image:: img/webdavnav_config-0.png
.. |image10| image:: img/webdavnav_browse-0.png
.. |image11| image:: img/scanbot_ajout_webdav.png
.. |image12| image:: img/scanbot_choix_webdav.png
.. |image13| image:: img/scanbot_config_webdav.png
.. |image14| image:: img/clip_image028.png
.. |image15| image:: img/clip_image030.png
.. |image16| image:: img/clip_image032.png
.. |image17| image:: img/signer_PDF_avec_GoFAST.png
.. |image18| image:: img/scanbot_envoi_GoFAST.png
.. |image19| image:: img/abbyy_hot_folder.png
.. |image20| image:: img/abbyy_hot_folder_config-0.png
