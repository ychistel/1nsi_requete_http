Modèle client serveur
======================

HTTP est un protocole qui permet de récupérer des ressources d'un serveur web comme les documents HTML, des images ou des médias. Il est à la base de tout échange de données sur le Web. C'est un protocole de type **client-serveur**.

.. figure:: ../img/modele_client_serveur_2.svg
    :align: center
    :width: 480

Le protocole HTTP se déroule en 2 temps:

#.  Le client initie la requête HTTP en demandant des ressources placées sur le serveur.
#.  Le serveur reçoit la requête HTTP, cherche les ressources demandées et envoie une réponse au client.

Les principales applications qui réalisent des requêtes HTTP sont les navigateurs comme **edge**, **firefox** ou **chrome**.

D'autres applications peuvent effectuer des requêtes HTTP.

-   Par exemple en **ligne de commande** avec le programme **CURL** la commande **linux** ``wget``.
-   Avec un langage de programmation : en Python, le module **requests** permet d'effectuer des requêtes HTTP pour récupérer des données sur un seveur web.

La requête HTTP
---------------

Une **requête HTTP** contient plusieurs informations utiles pour le serveur qui reçoit la requête :

-   la méthode utilisée (``GET`` ou ``POST``), 
-   le nom de la ressource (fichier) que l'on souhaite récupérer, 
-   le protocole utilisé et de sa version (HTTP en version 1 ou 2)
-   le destinataire ``HOST`` de la requête.

.. figure:: ../img/requete_client.svg
    :alt: modele client serveur
    :align: center
    :width: 300

    Requête HTTP d'un client

.. rubric:: La méthode GET

Dans un navigateur, la méthode ``GET`` est utilisée par défaut. Elle est accompagnée de plusieurs informations envoyées au serveur web:

-   le nom de la ``ressource`` demandée,
-   le protocole utilisé donc ``HTTP`` ainsi que sa version ``1`` ou ``2``,
-   le destinataire ou ``host`` de la requête qui correspond au serveur web.

.. rubric:: Méthode GET avec des paramètres

Une requête ``HTTP`` peut envoyer des ``paramètres`` au serveur web avec la méthode ``GET``. Le serveur traite la requête et adapte sa réponse selon les valeurs données aux paramètres.

.. warning::

    Les paramètres sont prédéfinis sur le serveur sans quoi ils sont ignorés.

La syntaxe d'une requête ``GET`` avec des paramètres est la suivante:

-  un ``point d'interrogation`` pour séparer l'url des paramètres,
-  ensuite les paramètres et les valeurs reliées par le signe ``égal``,
-  de plus les différents paramètres sont séparés par des ``esperluettes``.
-  les espaces entre les valeurs d'un paramètre sont remplacés par les signes ``plus``.

.. admonition:: Exemple

    On effectue une recherche sur un moteur de recherche sur les mots ``python`` et ``requête``. Le navigateur construit une requête avec la méthode ``GET`` en y ajoutant des paramètres.

    La requête ``HTTP`` envoyée au serveur avec la méthode ``GET`` a pour valeur: ``https://www.google.fr/search?q=python+requête``.

    .. figure:: ../img/requete_parametre_1.png
        :align: center
        :width: 560

        requête ``HTTP`` avec la méthode ``GET`` et des paramètres


.. rubric:: La méthode POST

La méthode ``POST`` permet d'envoyer des valeurs au serveur qui pourra les traiter. Les valeurs envoyées sont placées dans un tableau. Ce tableau, dit associatif, est placé dans le **corps de la requête** et non dans l'url comme avec la méthode ``GET``. Cela permet de mieux sécuriser l'envoi de données vers le serveur.

Pour envoyer des valeurs à un serveur web, on peut utiler un **formulaire**. Chaque champ de formulaire complété est associé à un paramètre. Un bouton d'envoi exécute la requête ``HTTP`` qui envoie les données vers le serveur.

.. admonition:: Exemple

    Un blog contient une page d'authentification qui permet d'accéder à des contenus privés.

    La page web de connexion contient un formulaire avec 2 champs **login** et **mot de passe**.

    .. image:: ../img/login_blogs.png
        :align: center
        :width: 300

    Après avoir renseigné ces deux champs, on valide le formulaire et le navigateur effectue une requête avec la méthode ``POST``. Les valeurs saisies sont envoyées au serveur sous la forme d'un tableau associatif au format ``JSON`` :

    .. code:: json

        {'user_id' : 'bob', 'user_pwd':'lép0nGe'}

    Les données ne sont pas ajoutées à l'url ! Si tel était le cas, ce serait un problème pour la sécurité et la confidentialité des données. Les données de la requête ``POST`` sont placées dans le corps de la requête.

La réponse du serveur
----------------------

Quelle que soit la méthode utilisée par le **client**, le serveur répond à la requête ``HTTP``. Sa réponse contient un code d'état, un statut et la ressource demandée.

.. figure:: ../img/reponse_serveur.svg
    :alt: modele client serveur
    :align: center
    :width: 300

    Réponse HTTP du serveur

Les codes d'état sont classés selon leurs statuts. Les plus courants sont :

-  Si le statut de la requête est un succès, le code d'état vaut ``200``;
-  Si le statut de la requête a été redirigée vers un autre site web, le code d'état vaut ``301``;
-  Si le statut de la ressource n'est pas accessible, accès refusé, le code d'état vaut ``403``;
-  Si le statut de la ressource demandée n'est pas trouvée, le code vaut ``404``;
-  Si le serveur ne peut pas répondre (panne), le code vaut ``500``;

Suite à la requête d'un client avec la méthode ``GET``, le serveur traite la requête et répond. Si la ressource demandée est trouvée, il la renvoie avec le code d'état 200.

Avec la ressource demandée, un en-tête de réponse est ajouté et contient les éléments suivants:

.. admonition:: Exemple

    Suite à une requête ``HTTP``, le serveur renvoie la ressource et un en-tête de réponse contenant différentes informations:

    -   Le type de contenu et son encodage : text/html; charset=UTF-8
    -   la taille du contenu : 28722 octets.
    -   La date et l'heure de l'envoi : 29 mars 2022
    -   Le serveur utilise l'application **Apache** qui est un serveur WEB,
    -   La connexion est fermée après l'envoi.