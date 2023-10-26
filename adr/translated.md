# ADR-007: Sélection de GitHub comme plateforme d'hébergement de code

## Résumé exécutif
Cette ADR documente la décision de sélectionner GitHub comme plateforme principale pour héberger, gérer et partager du code au sein du Lab IA (Intelligence Artificielle) de l'ACIA (Agence Canadienne d'Inspection des Aliments).

## Contexte
L'équipe a besoin d'une plateforme pour pouvoir gérer et partager du code qui doit être une plateforme en ligne afin que les membres de l'équipe puissent travailler ensemble en temps réel de n'importe où dans le pays et permettre également l'accès aux contributeurs externes du monde entier. Comme l'agence doit respecter la norme numérique du gouvernement du Canada et utiliser une approche open source, il est important de choisir la bonne plateforme qui aiderait à organiser et à vérifier le code.

## Décision
GitHub s'est clairement distingué des autres options disponibles pour plusieurs raisons:

* Communauté et focus sur l'open-source
    * GitHub bénéficie d'une communauté de développeurs plus importante et est mieux adapté pour le développement de code open-source et les projets open-source. C'est une plateforme où les programmeurs du monde entier collaborent sur des projets, souvent avec des niveaux de connaissance et d'engagement variables.

* Contrôle des versions
    * L'innovation continue de GitHub a aidé la plateforme à rester pertinente pendant de nombreuses années (créée en 2008).

* Automatisation de pipeline avec les actions GitHub
    * Flux de travail réutilisables : La marketplace de GitHub fournit une plateforme aux développeurs pour partager et réutiliser les workflows, réduisant le besoin de recréer des configurations de workflow communes. Ceci est particulièrement utile pour les tâches communes et les processus standard à travers les projets.

    * Intégration extensive : Il offre une gamme d'intégrations et d'actions tierces qui peuvent étendre les capacités de vos projets sur GitHub. Vous pouvez trouver des outils pour la surveillance, les tests, le déploiement, et plus encore.

    * Conduite par la communauté : La marketplace est conduite par la communauté, ce qui signifie que les développeurs peuvent contribuer leurs propres actions et workflows, faisant de celle-ci un riche écosystème d'outils et de processus d'automatisation. Ceci est particulièrement avantageux pour les projets open-source, car cela favorise la collaboration et le partage des ressources.

* Alignement avec Microsoft:
    * Car GitHub est détenu par Microsoft, ce qui aidera le laboratoire à rester en accord avec l'exigence de la politique du Cloud First du gouvernement du Canada. Cela fait en sorte que les contrats et les opérations soient cohérents.

    * Les contributions majeures de Microsoft à GitHub ont rendu la plateforme plus utile.

    * GitHub compte une énorme communauté d'utilisateurs, avec 4 millions d'organisations, 330 millions de dépôts utilisés par 90% des entreprises du Fortune 100, ce qui montre sa fiabilité et sa large acceptation dans l'industrie. Cela montre que GitHub est largement connu, testé et très stable.

## Alternatives envisagées

### Alternative 1: GitLab
Pour :
* Plateforme Iron Mountain avec GitLab ultimate :
    * 50k d'économies estimées par an.

    * 20 heures économisées sur le temps d'intégration par projet.

* Logiciel IA intégré.

* Les données des utilisateurs ne sont pas utilisées pour former l'IA.

* Plateforme DevSecOps : Supports d'équipes en développement logiciel.

* Classée Leader dans le Quadrant Magique de Gartner® for DevOps Platforms.

* 30m + d'utilisateurs inscrits.

* Utilisé par plus de 50% du Fortune 100.

Contre :
* La navigation dans l'interface peut être difficile, surtout pour les nouveaux utilisateurs.

* La personnalisation du suivi des problèmes est limitée pour certains utilisateurs.

* Certaines revues signalent un manque de documentation.

* Intégration CI/Automation.

### Alternative 2: Azure DevOps
Pour :
* Azure DevOps inclut Azure Boards, un outil de gestion de projets qui permet de suivre des éléments de travail, tels que des histoires utilisateur, des tâches, des bugs et des fonctionnalités. Cette fonction est utile pour ceux qui suivent des méthodes agiles.

* Azure Test Plans est un outil de test qui vous permet de planifier, d'exécuter et de suivre des tests manuels et automatisés.

* S'intègre facilement avec d'autres services Azure et produits Microsoft comme Visual Studio, Office 365, Azure, etc.

Contre :
* Principalement adapté aux développeurs.

* Communauté open-source moins proéminente par rapport à GitHub.

* Peut être très accablant et complexe pour les petites équipes car il offre beaucoup de services et de fonctionnalités qui ne sont pas toujours utiles pour les petits projets.

* La tarification est basée sur le nombre d'utilisateurs, de pipelines, d'agents, d'espace de stockage, etc. Vous pourriez finir par payer plus que vous ne le feriez avec d'autres plateformes ou outils.

### Alternative 3: Bitbucket
Pour :
* Support de Mercurial ainsi que Git pour le contrôle des versions.

* Support des fonctionnalités de recherche sémantique telles que les classes, les interfaces, etc., ce qui économise beaucoup de temps.

* Vous permet de donner aux développeurs un accès à toutes les branches d'un dépôt ou de restreindre l'accès à une seule branche, ce qui réduit le risque de poussée accidentelle sur la branche maîtresse/principale, c'est un facteur clé de différenciation pour Bitbucket.

* Bitbucket supporte Git Large File Storage (LFS) ce qui signifie des temps de clonage et de récupération plus courts pour ceux qui travaillent avec de gros fichiers.

Contre :
* Défis avec les outils ou plateformes externes.

* Limitations de fonctionnalités et moins axée sur la communauté.

* Pas de fonctionnalités intégrées de Continuous Integration/Continuous Deployment.

## Conséquences

La décision d'utiliser GitHub aidera le Lab IA de l'ACIA à étendre son portée, cela attirera plus de monde à examiner les produits et soutiendra les objectifs open source. Cela facilitera également beaucoup le DevOps avec sa grande marketplace pour le workflow. Cela aidera également les développeurs à être plus productifs et à améliorer leur travail. Cela dit, le Lab IA de l'ACIA dispose d'une équipe de développement logiciel et d'une équipe de Data Science, une équipe utilise GitHub et l'autre utilise Azure DevOps, ce qui pourrait entraîner quelques complications.

## Références
[GetApp * Avis sur GitLab](https://www.getapp.com/fr/it-management-software/a/gitlab/reviews/#:~:text=Pros.%20Its%20intuitive%20interface%20and%20robust%20feature%20set,challenging%20for%20new%20users%20to%20get%20started.%20IR)

[TrustRadius * Avantages et inconvénients de GitLab 2023](https://www.trustradius.com/products/gitlab/reviews)

[Vince The IT Guy * Avantages et inconvénients pour l'utilisation de GitLab](https://vincetheitguy.com/gitlab-pros-and-cons/)

[Capiche * Avantages et inconvénients de GitLab](https://capiche.com/q/gitlab-pros-and-cons)

[TrustRadius * Avis sur les services Azure DevOps](https://www.trustradius.com/products/azure-devops-services/reviews?qs=pros-and-cons)

[Software Advice * Avis sur le logiciel Azure DevOps Services, avantages et inconvénients * 2023](https://www.softwareadvice.com/devops/azure-devops-profile/reviews/)

[Dev.to * Azure DevOps vs GitHub: Quelle pile d'outils est la meilleure pour les équipes logicielles?](https://dev.to/devteams/azure-devops-vs-github-which-toolstack-is-better-for-software-teams)

[StackShare * Avis, avantages et inconvénients | Entreprises utilisant Azure DevOps](https://stackshare.io/azure-devops)

[TrustRadius * Avantages et inconvénients de Bitbucket 2023](https://www.trustradius.com/products/bitbucket/reviews)

[Sysgeeker * Bitbucket Review * Rationalisez Votre Effort de Collaboration de Code sans Effort](https://www.sysgeeker.com/bitbucket-review.html)

[CompareCamp * BitBucket Review: Pricing, Avantages, Inconvénients et Caractéristiques](https://comparecamp.com/bitbucket-review-pricing-pros-cons-features/)

[Capterra * Avis Bitbucket 2023](https://www.capterra.com/p/166497/Bitbucket/reviews/)

[https://about.gitlab.com/customers/iron-mountain/](https://about.gitlab.com/customers/iron-mountain/)\n\n
