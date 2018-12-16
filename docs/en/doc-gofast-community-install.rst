********************************************
GoFAST Community :  Installation
********************************************

Instructions (par image)
------------

–Step 1: Download the image https://www.ceo-vision.com/fr/content/gofast-community-ged-plateforme-collaborative-opensource (.ova, ...)

–Step 2: Start the instance on your VirtualMachine 

–Step 3: Login to your instance with the follwing inforamtions: 

``login : root`` ``password : @C0mmunity!`` (with a 0 not O) 

–Step 4: Configure the IP address in for example  ``/etc/sysconfig/network-scripts/ifcfg-enp0s3`` 
and enter IPADDR  =  Choosen address instead of “192.168.8.212”

–Step 5: Definie the FQDN ex. ``gofast-community.mydomain.com`` corresponding to your IP in your hosts file or DNS

–Step 6: Enter ``https://gofast-community.mydomain.com`` and configure the platform

Configuration
-------------

.. figure:: /media-guide/Logo-Community.png
   :alt: 

Pour toutes les informations concernant les pré-requis et l'installation de GoFAST sur le serveur, 
veuillez vous diriger vers cette page : https://gofast-docs.readthedocs.io/fr/latest/docs-gofast-technical/gofast-docs-prerequis-installation-serveur.html#gofast-pre-requis-et-installation-serveur


.. note:: Afin de pouvoir configurer votre GoFAST Community, vous devez tout d'abord vous rendre sur l'adresse IP correspondant à votre serveur (sur lequel vous avez instancié GoFAST). 
          Example : http://35.180.66.5

5 steps are required to finish the GoFAST Community configuration : 

* Change name domaine
* Configure SSL Certificate
* Configure SMTP Server
* Create Admin User
* Finish Configuration 

You will find below detailed configuration for every steps and what is the purpose of every fields requiered.

Step 1 : Define Domain Name
-------------------

Configuration screen looks like: 

.. figure:: /media-guide/Change-Name-Domaine.png 

On this screen you will describe every part of the FQDN of GoFAST, ex. ``gofast.ceo-vision.com`` : 

   1. **New Sub-Domain** : This is the subdomain of the GoFAST, ex. ``gofast.``
   2. **New Domain** : This is usualy the domain of your organisation ex. ``ceo-vision`` 
   3. **New extension** : This is the TLD, the last part of the url ex. ``com`` 


Etape 2 : Configure SSL Certificate 
-----------------------------------

At this step you will have 2 configuraiton possibilities.

.. figure:: /media-guide/Configure-SSL-1.png 
   :alt: 

The first option (recommended) is to upload your own SSL certificates 
  - **Key Private** :
  - **Key Public** :

The second option gives you the ability to create a self signed certificate. 
Several mandatory fields will be requested :

.. figure:: /media-guide/Configure-SSL-1-modified.png 
   :alt:
   
.. figure:: /media-guide/Configure-SSL-Certificate-2.png
   :alt: 
      
   1. **Country**
   2. **State or Province**
   3. **City**
   4. **Company** 
   5. **Organization unit** 
   6. **Web site name**
   7. **E-mail address** 



Step 3 : Configure SMTP Server 
-------------------------------

This third step will help you to configure the SMTP server used by GoFAST: 

.. figure:: /media-guide/Configure-SMTP-1.png
   :alt:
   
.. figure:: /media-guide/Configure-SMTP-2.png
   :alt: 
   
The different fields requested : 

   1. **SMTP Server** :  
   2. **Username** : 
   3. **Password** : 
   4. **Security** : None (without security), TLS (....), SSL (....)
   5. **SMTP Port** : 
   6. **Recipient address** : 


Step 4 : Create Admin User
---------------------------

This step will define the 'administrator' account who will have access to several configurations once the GoFAST instance is started

You will have to choose a login, password and email address linked to this 'admin' account 

.. figure:: /media-guide/Create-Admin-User-1.png
   :alt:
   
.. figure:: /media-guide/Create-Admin-User-2.png
   :alt:


Step 5 : Finish Configuration 
------------------------------

This last step is a summary of all informations entered in the previous steps for your GoFAST Community

.. WARNING :: 
   After clicking on "Finish Configuration" you will not be able to come back to the previous steps, 
   please check every fields before submitting 

.. figure:: /media-guide/Finish-Configuration-Community.png
   :alt: 
   


   
