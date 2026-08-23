#ifndef VINDEX_FENESTRALE_II_COMPOSITOR_K_ABI_H
#define VINDEX_FENESTRALE_II_COMPOSITOR_K_ABI_H

/* Sylvia OS — Fenestrale II, Gradus K.
 * Eventa compositorii ad clientes VINDEX in campis reservatis mailbox G.
 * Extensio additiva est; ABI Gradus G neque mensura mailbox mutantur.
 */

#include "fenestrale_ii_compositor_abi.h"

#define FII_CMP_OP_EVENTUM              8ULL

#define FII_CMP_EVENTUM_NULLUM          0ULL
#define FII_CMP_EVENTUM_FOCUS           1ULL
#define FII_CMP_EVENTUM_DIMENSIO        2ULL

#define FII_CMP_EVENTUM_ARG_TYPUS       0U
#define FII_CMP_EVENTUM_ARG_PRIMUM      1U
#define FII_CMP_EVENTUM_ARG_SECUNDUM    2U

#define FII_CMP_FOCUS_INACTIVUS         0ULL
#define FII_CMP_FOCUS_ACTIVUS           1ULL

#endif /* VINDEX_FENESTRALE_II_COMPOSITOR_K_ABI_H */
