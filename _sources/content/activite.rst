Activité
========

Le **web** est un ensemble de serveurs sur internet proposant des contenus disponibles sous forme de page écrites au format **html**. Ces pages contiennent du texte, des images, des médias et permettent aussi d’envoyer et recevoir des données.

Pour accéder à ces multiples ressources, il est nécessaire d’utiliser des logiciels appelés navigateurs qui établissent une communication avec les serveurs de contenus web.

Comme dans toute communication, des règles sont nécessaires pour assurer l’envoi et la réception des données. Ces règles sont réunies dans un protocole. Le protocole utilisé pour le web est le protocole HTTP et s’effectue dans un **modèle** dit **client - serveur**.

.. figure:: ../img/modele_client_serveur_1.svg
   :alt: modele client serveur
   :align: center
   :width: 480

Ce protocole permet la communication entre 2 machines, l’une étant le client et l’autre le serveur:

-  Le client initie la communication en réalisant une **requête HTTP**;
-  Le serveur reçoit la requête et envoie au client une **réponse HTTP**.

Une **requête HTTP** est composée d'une méthode, de la ressource web souhaitée, du protocole utilisé et de sa version et le destinataire de la requête.

.. figure:: ../img/requete_client.svg
   :alt: modele client serveur
   :align: center
   :width: 300

   Requête HTTP d'un client
   
Le serveur répond toujours à une requête HTTP qu’il reçoit. La **réponse HTTP** est composée du protocole et de sa version, du code d’état et du statut HTTP. Dans le cas où la ressource est trouvée, celle-ci est envoyée au serveur.

.. figure:: ../img/reponse_serveur.svg
   :alt: modele client serveur
   :align: center
   :width: 300

   Réponse HTTP du serveur



On met à disposition un fichier qui simule un serveur, un serveur DNS et un réseau local constitué de 3 portables. On donne les informations suivantes:

-  adresse du réseau local : ``192.168.0.0/24``
-  adresse IP du serveur web : ``172.16.0.20``
-  adresse IP du serveur DNS : ``172.16.0.10``

Le fichier filius de ce réseau est à télécharger : :download:`réseau filius <../filius/reseau_web.fls>`

Les serveurs sont déjà configurés et le portable A est prêt à l'emploi. Le server web héberge une page web accessible à l'adresse ``http://www.nsi.org``.

#. Sur le portable A, saisir l'adresse pour afficher la page web du serveur et contrôler que tout est fonctionnel.
#. Afficher la table des échanges du portable A puis sélectionner la première trame de la couche "Application".

   a) Quelles sont les données transmises dans la requête ? Quel protocole est utilisé ?
   b) Quel serveur répond à cette requête ? Quelle est sa réponse ?

#. On analyse la première trame de la couche "Application" utilisant le protocole "http".

   a) Quel est le contenu de la requête http ?
   b) Quel serveur répond à cette requête ? Quelle est sa réponse ?

#. Suite à la réponse du serveur, une nouvelle requête http est envoyée.

   a) Quel le contenu de la requête envoyée ?
   b) Expliquer pourquoi cette seconde requête est envoyée au serveur.
   c) Quelle est la réponse du serveur ?
   d) Combien de trames sont nécessaires pour envoyer le contenu associé à la réponse. Justifier puis donner la taille totale du contenu envoyé.
