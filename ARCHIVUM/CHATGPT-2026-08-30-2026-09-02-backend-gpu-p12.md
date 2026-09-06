# Session ChatGPT — Backend Graphica X et P12 matériel

_Reconstruction de coordination, non verbatim._
_La transcription intégrale de cette période n'est pas disponible dans les partages récupérables. Ce fichier conserve les décisions et résultats recoupés avec les PR/commits canoniques._
_Période couverte : 30 août – 5 septembre 2026._
_Sources de contrôle : PR #157–#165, #171/#172, #160/#161/#164/#166/#167._

---

## Principe directeur

Le backend matériel ne doit jamais être simulé par un drapeau. Tant qu'une opération n'est pas réellement exécutée par le GPU, le backend logiciel reste l'oracle sémantique et le système doit annoncer honnêtement son fallback.

## P16-XII-F1 à F8

    [action] F1/#157 : séparation compositeur/exécuteur, contrat backend et file graphique.
    [action] F2/#158 : cache de textures, générations, LRU, verrous et invalidation ; pixels inchangés.
    [action] F3/#159 : batch explicite COPIA/COMPONE/NOVEM/PRAESENTA, fences et abandon sûr ; la composition du backbuffer et la présentation sont deux étapes/fences distinctes.
    [action] F4/#162 : cycle de vie transactionnel CREATE/RENEW/FREE des textures avec rollback.
    [action] F5/#163 : liaison automatique cache ↔ cycle de vie des ressources.
    [action] F6/#165 : contrat d'exécuteur unique ; aucun faux fence après échec.
    [action] F7/#171 : vrai présentateur VirtIO GPU 2D, `TRANSFER_TO_HOST_2D` + `RESOURCE_FLUSH` sur damage.
    [action] F8/#172 : le backbuffer Graphica X devient directement la mémoire DMA présentée ; suppression de la copie CPU intermédiaire.

La preuve F8 canonique encode `D = Z = 1 028 096` pixels : dans cette preuve, chaque pixel transféré vient directement de la surface DMA Graphica X, sans seconde copie CPU de présentation.

## P12-V1 à V4

    [action] #160 : BAR PCI 64 bits et restauration sûre ; nombre de BAR borné selon le type d'en-tête.
    [action] #161 : MMIO 8/16/32/64 borné, permissions, `MFENCE`, lecture e1000e réelle.
    [action] #164 : pages DMA physiques UEFI, zéroisation, direction et libération réelles.
    [action] #166 : syntaxe/ABI `INTERRUPTIO`, IDT et MSI réel sous QEMU EDU.
    [action] #167 : transport VirtIO PCI moderne, virtqueue DMA et premier `GET_DISPLAY_INFO` réel.

## Discipline de recanonisation

Plusieurs branches historiques contenaient des piles devenues obsolètes. La méthode retenue est de reconstruire chaque incrément directement sur le `main` moderne et de ne transporter que son delta fonctionnel. Cela évite de réintroduire un ancien `CONSILIUM`, un vieux compilateur ou une dépendance déjà canonisée ailleurs.

## Ce qui a été écarté

- Revendiquer « GPU actif » sans commande matérielle réellement consommée.
- Fusionner en bloc d'anciennes piles empilées alors que leurs bases avaient changé.
- Publier une fence après un batch abandonné ou échoué.