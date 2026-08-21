#define _GNU_SOURCE

#include <ctype.h>
#include <dlfcn.h>
#include <errno.h>
#include <fcntl.h>
#include <limits.h>
#include <stdarg.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

/*
 * VINDEX Graphica 0.36 — adaptator GTK declarativus.
 *
 * Hic pons nullam Officinae structuram novit. Formam textualem legit,
 * elementa GTK creat, valores exportat, eventa unius octeti ad programma
 * VINDEX mittit et responsa declarata applicat. Logica applicationis manet
 * in fonte VINDEX et in archivo .forma.
 */

typedef void GtkWidget;
typedef void GtkTextBuffer;
typedef void GtkCssProvider;
typedef void GdkScreen;
typedef struct { uint64_t data[24]; } GtkTextIterSpatium;

enum {
    GTK_WINDOW_TOPLEVEL = 0,
    GTK_ORIENTATION_HORIZONTAL = 0,
    GTK_ORIENTATION_VERTICAL = 1,
    GTK_POLICY_AUTOMATIC = 1,
    GTK_WRAP_NONE = 0,
    GTK_FILE_CHOOSER_ACTION_OPEN = 0,
    GTK_FILE_CHOOSER_ACTION_SAVE = 1,
    GTK_RESPONSE_CANCEL = -6,
    GTK_RESPONSE_ACCEPT = -3,
    GTK_STYLE_PROVIDER_PRIORITY_APPLICATION = 600,
};

typedef struct {
    int (*gtk_init_check)(int *, char ***);
    GtkWidget *(*gtk_window_new)(int);
    void (*gtk_window_set_title)(void *, const char *);
    void (*gtk_window_set_default_size)(void *, int, int);
    int (*gtk_window_set_icon_from_file)(void *, const char *, void **);
    void (*gtk_container_set_border_width)(void *, unsigned int);
    void (*gtk_container_add)(void *, void *);
    GtkWidget *(*gtk_box_new)(int, int);
    void (*gtk_box_pack_start)(void *, void *, int, int, unsigned int);
    void (*gtk_box_pack_end)(void *, void *, int, int, unsigned int);
    GtkWidget *(*gtk_button_new_with_label)(const char *);
    void (*gtk_button_set_label)(void *, const char *);
    GtkWidget *(*gtk_label_new)(const char *);
    void (*gtk_label_set_text)(void *, const char *);
    void (*gtk_label_set_xalign)(void *, float);
    GtkWidget *(*gtk_entry_new)(void);
    void (*gtk_entry_set_text)(void *, const char *);
    const char *(*gtk_entry_get_text)(void *);
    void (*gtk_entry_set_placeholder_text)(void *, const char *);
    GtkWidget *(*gtk_text_view_new)(void);
    GtkTextBuffer *(*gtk_text_view_get_buffer)(void *);
    void (*gtk_text_view_set_monospace)(void *, int);
    void (*gtk_text_view_set_wrap_mode)(void *, int);
    void (*gtk_text_view_set_left_margin)(void *, int);
    void (*gtk_text_view_set_right_margin)(void *, int);
    void (*gtk_text_view_set_top_margin)(void *, int);
    void (*gtk_text_view_set_bottom_margin)(void *, int);
    void (*gtk_text_view_set_editable)(void *, int);
    void (*gtk_text_buffer_set_text)(void *, const char *, int);
    void (*gtk_text_buffer_get_bounds)(void *, void *, void *);
    char *(*gtk_text_buffer_get_text)(void *, const void *, const void *, int);
    GtkWidget *(*gtk_scrolled_window_new)(void *, void *);
    void (*gtk_scrolled_window_set_policy)(void *, int, int);
    GtkWidget *(*gtk_paned_new)(int);
    void (*gtk_paned_pack1)(void *, void *, int, int);
    void (*gtk_paned_pack2)(void *, void *, int, int);
    void (*gtk_paned_set_position)(void *, int);
    GtkWidget *(*gtk_separator_new)(int);
    void (*gtk_widget_set_name)(void *, const char *);
    void (*gtk_widget_add_events)(void *, int);
    void (*gtk_widget_set_size_request)(void *, int, int);
    void (*gtk_widget_set_sensitive)(void *, int);
    void (*gtk_widget_set_tooltip_text)(void *, const char *);
    void (*gtk_widget_show_all)(void *);
    void (*gtk_widget_destroy)(void *);
    GtkWidget *(*gtk_file_chooser_dialog_new)(const char *, void *, int, const char *, ...);
    int (*gtk_dialog_run)(void *);
    char *(*gtk_file_chooser_get_filename)(void *);
    int (*gtk_file_chooser_set_filename)(void *, const char *);
    void (*gtk_file_chooser_set_current_name)(void *, const char *);
    GtkCssProvider *(*gtk_css_provider_new)(void);
    int (*gtk_css_provider_load_from_data)(void *, const char *, long, void **);
    void (*gtk_style_context_add_provider_for_screen)(void *, void *, unsigned int);
    void (*gtk_main)(void);
    void (*gtk_main_quit)(void);
    unsigned long (*g_signal_connect_data)(void *, const char *, void (*)(void), void *, void *, int);
    void (*g_object_unref)(void *);
    void (*g_free)(void *);
    unsigned int (*g_timeout_add)(unsigned int, int (*)(void *), void *);
    GdkScreen *(*gdk_screen_get_default)(void);
    int (*gdk_event_get_keyval)(const void *, unsigned int *);
    int (*gdk_event_get_button)(const void *, unsigned int *);
    int (*gdk_event_get_coords)(const void *, double *, double *);
} GtkApi;

typedef enum {
    GENUS_FENESTRA, GENUS_VERTICALIS, GENUS_HORIZONTALIS, GENUS_TITULUS,
    GENUS_BULLA, GENUS_EDITOR, GENUS_EXITUS, GENUS_CAMPUS_TEXTUS,
    GENUS_DIVISOR, GENUS_SEPARATOR
} GenusElementi;

typedef enum {
    ACTIO_TEXTUS, ACTIO_TEXTUS_ARCHIVO, ACTIO_SENSIBILIS, ACTIO_NOVUM,
    ACTIO_APERI, ACTIO_SERVA, ACTIO_TITULUS_FENESTRAE, ACTIO_CLAUDE
} GenusActionis;

struct Graphica;

typedef struct {
    struct Graphica *graphica;
    char id[64];
    GenusElementi genus;
    GtkWidget *widget;
    GtkWidget *internum;
    GtkTextBuffer *receptaculum;
    int eventum;
    int eventum_clavis;
    int eventum_muris;
    int eventum_mutationis;
    char via[PATH_MAX];
} Elementum;

typedef struct {
    unsigned char responsum;
    GenusActionis genus;
    char destinatio[64];
    char auxilium[64];
    char textus[1024];
    char via[PATH_MAX];
    int numerus;
} Actio;

#define MAX_ELEMENTA 128
#define MAX_ACTIONES 256
#define MAX_CAMPI 16

typedef struct Graphica {
    GtkApi api;
    void *libgtk;
    void *libgobject;
    void *libglib;
    void *libgdk;
    Elementum elementa[MAX_ELEMENTA];
    size_t numerus_elementorum;
    Actio actiones[MAX_ACTIONES];
    size_t numerus_actionum;
    GtkWidget *fenestra_principalis;
    char directorium_formae[PATH_MAX];
    const char *fons_initialis;
    int modus_servitoris;
    int canalis_ad_vindex;
    int canalis_ab_vindex;
    unsigned char eventum_clausurae;
} Graphica;

static const char *CANALIS_AD_VINDEX = ".vindex-graphica-ad-vindex";
static const char *CANALIS_AB_VINDEX = ".vindex-graphica-ab-vindex";

static void nuntia(const char *forma, ...) {
    va_list ap;
    va_start(ap, forma);
    vfprintf(stderr, forma, ap);
    va_end(ap);
}

static int symbolum(void *lib, void **destinatio, const char *nomen) {
    dlerror();
    *destinatio = dlsym(lib, nomen);
    const char *erratum = dlerror();
    if (erratum != NULL || *destinatio == NULL) {
        nuntia("ERRATUM: symbolum GTK deest: %s\n", nomen);
        return 0;
    }
    return 1;
}

#define RESOLVE(lib, membrum) \
    do { if (!symbolum((lib), (void **)&graphica->api.membrum, #membrum)) return 0; } while (0)

static int onera_gtk(Graphica *graphica) {
    graphica->libgtk = dlopen("libgtk-3.so.0", RTLD_NOW | RTLD_LOCAL);
    graphica->libgobject = dlopen("libgobject-2.0.so.0", RTLD_NOW | RTLD_LOCAL);
    graphica->libglib = dlopen("libglib-2.0.so.0", RTLD_NOW | RTLD_LOCAL);
    graphica->libgdk = dlopen("libgdk-3.so.0", RTLD_NOW | RTLD_LOCAL);
    if (!graphica->libgtk || !graphica->libgobject || !graphica->libglib || !graphica->libgdk) {
        nuntia("ERRATUM: GTK 3 in hoc systemate non invenitur.\n");
        return 0;
    }
    RESOLVE(graphica->libgtk, gtk_init_check);
    RESOLVE(graphica->libgtk, gtk_window_new);
    RESOLVE(graphica->libgtk, gtk_window_set_title);
    RESOLVE(graphica->libgtk, gtk_window_set_default_size);
    RESOLVE(graphica->libgtk, gtk_window_set_icon_from_file);
    RESOLVE(graphica->libgtk, gtk_container_set_border_width);
    RESOLVE(graphica->libgtk, gtk_container_add);
    RESOLVE(graphica->libgtk, gtk_box_new);
    RESOLVE(graphica->libgtk, gtk_box_pack_start);
    RESOLVE(graphica->libgtk, gtk_box_pack_end);
    RESOLVE(graphica->libgtk, gtk_button_new_with_label);
    RESOLVE(graphica->libgtk, gtk_button_set_label);
    RESOLVE(graphica->libgtk, gtk_label_new);
    RESOLVE(graphica->libgtk, gtk_label_set_text);
    RESOLVE(graphica->libgtk, gtk_label_set_xalign);
    RESOLVE(graphica->libgtk, gtk_entry_new);
    RESOLVE(graphica->libgtk, gtk_entry_set_text);
    RESOLVE(graphica->libgtk, gtk_entry_get_text);
    RESOLVE(graphica->libgtk, gtk_entry_set_placeholder_text);
    RESOLVE(graphica->libgtk, gtk_text_view_new);
    RESOLVE(graphica->libgtk, gtk_text_view_get_buffer);
    RESOLVE(graphica->libgtk, gtk_text_view_set_monospace);
    RESOLVE(graphica->libgtk, gtk_text_view_set_wrap_mode);
    RESOLVE(graphica->libgtk, gtk_text_view_set_left_margin);
    RESOLVE(graphica->libgtk, gtk_text_view_set_right_margin);
    RESOLVE(graphica->libgtk, gtk_text_view_set_top_margin);
    RESOLVE(graphica->libgtk, gtk_text_view_set_bottom_margin);
    RESOLVE(graphica->libgtk, gtk_text_view_set_editable);
    RESOLVE(graphica->libgtk, gtk_text_buffer_set_text);
    RESOLVE(graphica->libgtk, gtk_text_buffer_get_bounds);
    RESOLVE(graphica->libgtk, gtk_text_buffer_get_text);
    RESOLVE(graphica->libgtk, gtk_scrolled_window_new);
    RESOLVE(graphica->libgtk, gtk_scrolled_window_set_policy);
    RESOLVE(graphica->libgtk, gtk_paned_new);
    RESOLVE(graphica->libgtk, gtk_paned_pack1);
    RESOLVE(graphica->libgtk, gtk_paned_pack2);
    RESOLVE(graphica->libgtk, gtk_paned_set_position);
    RESOLVE(graphica->libgtk, gtk_separator_new);
    RESOLVE(graphica->libgtk, gtk_widget_set_name);
    RESOLVE(graphica->libgtk, gtk_widget_add_events);
    RESOLVE(graphica->libgtk, gtk_widget_set_size_request);
    RESOLVE(graphica->libgtk, gtk_widget_set_sensitive);
    RESOLVE(graphica->libgtk, gtk_widget_set_tooltip_text);
    RESOLVE(graphica->libgtk, gtk_widget_show_all);
    RESOLVE(graphica->libgtk, gtk_widget_destroy);
    RESOLVE(graphica->libgtk, gtk_file_chooser_dialog_new);
    RESOLVE(graphica->libgtk, gtk_dialog_run);
    RESOLVE(graphica->libgtk, gtk_file_chooser_get_filename);
    RESOLVE(graphica->libgtk, gtk_file_chooser_set_filename);
    RESOLVE(graphica->libgtk, gtk_file_chooser_set_current_name);
    RESOLVE(graphica->libgtk, gtk_css_provider_new);
    RESOLVE(graphica->libgtk, gtk_css_provider_load_from_data);
    RESOLVE(graphica->libgtk, gtk_style_context_add_provider_for_screen);
    RESOLVE(graphica->libgtk, gtk_main);
    RESOLVE(graphica->libgtk, gtk_main_quit);
    RESOLVE(graphica->libgobject, g_signal_connect_data);
    RESOLVE(graphica->libgobject, g_object_unref);
    RESOLVE(graphica->libglib, g_free);
    RESOLVE(graphica->libglib, g_timeout_add);
    RESOLVE(graphica->libgdk, gdk_screen_get_default);
    RESOLVE(graphica->libgdk, gdk_event_get_keyval);
    RESOLVE(graphica->libgdk, gdk_event_get_button);
    RESOLVE(graphica->libgdk, gdk_event_get_coords);
    return 1;
}

static void claude_gtk(Graphica *graphica) {
    if (graphica->libgdk) dlclose(graphica->libgdk);
    if (graphica->libglib) dlclose(graphica->libglib);
    if (graphica->libgobject) dlclose(graphica->libgobject);
    if (graphica->libgtk) dlclose(graphica->libgtk);
}

static int lege_archivum(const char *via, char **textus, size_t *magnitudo) {
    FILE *f = fopen(via, "rb");
    if (!f) return 0;
    if (fseek(f, 0, SEEK_END) != 0) { fclose(f); return 0; }
    long n = ftell(f);
    if (n < 0 || n > 1048576) { fclose(f); errno = EFBIG; return 0; }
    rewind(f);
    char *receptaculum = calloc((size_t)n + 1, 1);
    if (!receptaculum) { fclose(f); return 0; }
    size_t lectum = fread(receptaculum, 1, (size_t)n, f);
    int erratum = ferror(f);
    fclose(f);
    if (erratum) { free(receptaculum); return 0; }
    receptaculum[lectum] = '\0';
    *textus = receptaculum;
    *magnitudo = lectum;
    return 1;
}

static int scribe_archivum(const char *via, const char *textus, size_t magnitudo) {
    char temporarium[PATH_MAX];
    if (snprintf(temporarium, sizeof temporarium, "%s.XXXXXX", via) >= (int)sizeof temporarium) {
        errno = ENAMETOOLONG;
        return 0;
    }
    int fd = mkstemp(temporarium);
    if (fd < 0) return 0;
    size_t scriptum = 0;
    while (scriptum < magnitudo) {
        ssize_t n = write(fd, textus + scriptum, magnitudo - scriptum);
        if (n < 0 && errno == EINTR) continue;
        if (n <= 0) { close(fd); unlink(temporarium); return 0; }
        scriptum += (size_t)n;
    }
    if (fsync(fd) != 0 || close(fd) != 0 || rename(temporarium, via) != 0) {
        unlink(temporarium);
        return 0;
    }
    return 1;
}

static size_t disseca(char *linea, char **campi, size_t capacitas) {
    size_t n = 0;
    if (capacitas == 0) return 0;
    campi[n++] = linea;
    for (char *p = linea; *p; ++p) {
        if (*p == '\r' || *p == '\n') { *p = '\0'; break; }
        if (*p == '\t' && n < capacitas) {
            *p = '\0';
            campi[n++] = p + 1;
        }
    }
    return n;
}

static void textum_explica(const char *fons, char *exitus, size_t capacitas) {
    size_t j = 0;
    for (size_t i = 0; fons[i] && j + 1 < capacitas; ++i) {
        if (fons[i] == '\\' && fons[i + 1]) {
            ++i;
            if (fons[i] == 'n') exitus[j++] = '\n';
            else if (fons[i] == 't') exitus[j++] = '\t';
            else exitus[j++] = fons[i];
        } else exitus[j++] = fons[i];
    }
    exitus[j] = '\0';
}

static int numerum(const char *textus, int *valor) {
    char *finis = NULL;
    errno = 0;
    long v = strtol(textus, &finis, 10);
    if (errno || !finis || *finis || v < INT_MIN || v > INT_MAX) return 0;
    *valor = (int)v;
    return 1;
}

static int id_rectum(const char *id) {
    if (!id[0] || strlen(id) >= 64) return 0;
    for (const unsigned char *p = (const unsigned char *)id; *p; ++p) {
        if (!isalnum(*p) && *p != '_' && *p != '-') return 0;
    }
    return 1;
}

static int directoria_formae_pone(Graphica *graphica, const char *via) {
    char plena[PATH_MAX];
    if (!realpath(via, plena)) return 0;
    char *signum = strrchr(plena, '/');
    if (!signum) return 0;
    *signum = '\0';
    return snprintf(graphica->directorium_formae, sizeof graphica->directorium_formae,
                    "%s", plena) < (int)sizeof graphica->directorium_formae;
}

static int viam_resolve(Graphica *graphica, const char *species, char *exitus, size_t capacitas) {
    if (species[0] != '@') return snprintf(exitus, capacitas, "%s", species) < (int)capacitas;
    const char *relativa = species + 1;
    if (relativa[0] == '/') return snprintf(exitus, capacitas, "%s", relativa) < (int)capacitas;
    return snprintf(exitus, capacitas, "%s/%s", graphica->directorium_formae, relativa) < (int)capacitas;
}

static Elementum *elementum_inveni(Graphica *graphica, const char *id) {
    for (size_t i = 0; i < graphica->numerus_elementorum; ++i) {
        if (strcmp(graphica->elementa[i].id, id) == 0) return &graphica->elementa[i];
    }
    return NULL;
}

static Elementum *elementum_crea(Graphica *graphica, const char *id, GenusElementi genus) {
    if (!id_rectum(id) || elementum_inveni(graphica, id) ||
        graphica->numerus_elementorum >= MAX_ELEMENTA) return NULL;
    Elementum *elementum = &graphica->elementa[graphica->numerus_elementorum++];
    memset(elementum, 0, sizeof *elementum);
    elementum->graphica = graphica;
    elementum->genus = genus;
    snprintf(elementum->id, sizeof elementum->id, "%s", id);
    return elementum;
}

static int applica_parenti(Graphica *graphica, Elementum *elementum,
                           const char *parentis_id, const char *locus, int expande) {
    Elementum *parens = elementum_inveni(graphica, parentis_id);
    if (!parens) return 0;
    if (parens->genus == GENUS_FENESTRA) {
        graphica->api.gtk_container_add(parens->widget, elementum->widget);
        return 1;
    }
    if (parens->genus == GENUS_VERTICALIS || parens->genus == GENUS_HORIZONTALIS) {
        if (strcmp(locus, "FINIS") == 0)
            graphica->api.gtk_box_pack_end(parens->widget, elementum->widget, expande, expande, 0);
        else
            graphica->api.gtk_box_pack_start(parens->widget, elementum->widget, expande, expande, 0);
        return 1;
    }
    if (parens->genus == GENUS_DIVISOR) {
        if (strcmp(locus, "SECUNDUM") == 0)
            graphica->api.gtk_paned_pack2(parens->widget, elementum->widget, expande, 0);
        else
            graphica->api.gtk_paned_pack1(parens->widget, elementum->widget, expande, 0);
        return 1;
    }
    return 0;
}

static char *textus_elementi(Graphica *graphica, Elementum *elementum) {
    if (elementum->genus == GENUS_CAMPUS_TEXTUS) {
        const char *textus = graphica->api.gtk_entry_get_text(elementum->internum);
        return strdup(textus ? textus : "");
    }
    if (elementum->genus == GENUS_EDITOR || elementum->genus == GENUS_EXITUS) {
        GtkTextIterSpatium initium = {{0}};
        GtkTextIterSpatium finis = {{0}};
        graphica->api.gtk_text_buffer_get_bounds(elementum->receptaculum, &initium, &finis);
        return graphica->api.gtk_text_buffer_get_text(elementum->receptaculum, &initium, &finis, 1);
    }
    return NULL;
}

static void textum_elemento_pone(Graphica *graphica, Elementum *elementum, const char *textus) {
    const char *valor = textus ? textus : "";
    switch (elementum->genus) {
        case GENUS_TITULUS:
            graphica->api.gtk_label_set_text(elementum->internum, valor);
            break;
        case GENUS_BULLA:
            graphica->api.gtk_button_set_label(elementum->internum, valor);
            break;
        case GENUS_CAMPUS_TEXTUS:
            graphica->api.gtk_entry_set_text(elementum->internum, valor);
            break;
        case GENUS_EDITOR:
        case GENUS_EXITUS:
            graphica->api.gtk_text_buffer_set_text(elementum->receptaculum, valor, -1);
            break;
        default:
            break;
    }
}

static int exporta_valores(Graphica *graphica) {
    int recte = 1;
    for (size_t i = 0; i < graphica->numerus_elementorum; ++i) {
        Elementum *elementum = &graphica->elementa[i];
        if (elementum->genus != GENUS_EDITOR && elementum->genus != GENUS_CAMPUS_TEXTUS) continue;
        char *textus = textus_elementi(graphica, elementum);
        if (!textus) { recte = 0; continue; }
        char via[PATH_MAX];
        if (snprintf(via, sizeof via, ".vindex-graphica-valor-%s", elementum->id) >= (int)sizeof via ||
            !scribe_archivum(via, textus, strlen(textus))) recte = 0;
        graphica->api.g_free(textus);
    }
    return recte;
}

static int eventum_mitte(Graphica *graphica, unsigned char eventum) {
    if (!graphica->modus_servitoris || graphica->canalis_ad_vindex < 0) return 0;
    exporta_valores(graphica);
    for (;;) {
        ssize_t n = write(graphica->canalis_ad_vindex, &eventum, 1);
        if (n == 1) return 1;
        if (n < 0 && errno == EINTR) continue;
        return 0;
    }
}

static void cum_bulla(void *widget, void *datum) {
    (void)widget;
    Elementum *elementum = datum;
    if (elementum->eventum > 0 && elementum->eventum < 256)
        eventum_mitte(elementum->graphica, (unsigned char)elementum->eventum);
}

static void eventum_describe(Elementum *elementum, const char *textus) {
    char via[PATH_MAX];
    if (snprintf(via, sizeof via, ".vindex-graphica-eventum-%s", elementum->id) < (int)sizeof via)
        scribe_archivum(via, textus, strlen(textus));
}

static int cum_clavis(void *widget, void *eventum_gtk, void *datum) {
    (void)widget;
    Elementum *elementum = datum;
    unsigned int clavis = 0;
    char relatio[96];
    if (elementum->graphica->api.gdk_event_get_keyval(eventum_gtk, &clavis)) {
        snprintf(relatio, sizeof relatio, "CLAVIS\t%u\n", clavis);
        eventum_describe(elementum, relatio);
    }
    eventum_mitte(elementum->graphica, (unsigned char)elementum->eventum_clavis);
    return 0;
}

static int cum_mure(void *widget, void *eventum_gtk, void *datum) {
    (void)widget;
    Elementum *elementum = datum;
    unsigned int bulla = 0;
    double x = 0.0, y = 0.0;
    char relatio[128];
    elementum->graphica->api.gdk_event_get_button(eventum_gtk, &bulla);
    elementum->graphica->api.gdk_event_get_coords(eventum_gtk, &x, &y);
    snprintf(relatio, sizeof relatio, "MUS\t%u\t%.3f\t%.3f\n", bulla, x, y);
    eventum_describe(elementum, relatio);
    eventum_mitte(elementum->graphica, (unsigned char)elementum->eventum_muris);
    return 0;
}

static void cum_mutatione(void *widget, void *datum) {
    (void)widget;
    Elementum *elementum = datum;
    eventum_mitte(elementum->graphica, (unsigned char)elementum->eventum_mutationis);
}

static void cum_claude(void *widget, void *datum) {
    (void)widget;
    Graphica *graphica = datum;
    eventum_mitte(graphica, graphica->eventum_clausurae);
    graphica->api.gtk_main_quit();
}

static void titulum_viae_pone(Graphica *graphica, Elementum *titulus, const char *via) {
    if (!titulus) return;
    textum_elemento_pone(graphica, titulus, via && via[0] ? via : "fons nondum servatus");
}

static int editor_archivum_onera(Graphica *graphica, Elementum *editor,
                                 Elementum *titulus, const char *via, int retine_viam) {
    char *textus = NULL;
    size_t n = 0;
    if (!lege_archivum(via, &textus, &n)) return 0;
    (void)n;
    textum_elemento_pone(graphica, editor, textus);
    free(textus);
    if (retine_viam) snprintf(editor->via, sizeof editor->via, "%s", via);
    else editor->via[0] = '\0';
    titulum_viae_pone(graphica, titulus, retine_viam ? via : NULL);
    exporta_valores(graphica);
    return 1;
}

static int dialogum_aperi(Graphica *graphica, Elementum *editor, Elementum *titulus,
                          const char *inscriptio) {
    GtkWidget *dialogum = graphica->api.gtk_file_chooser_dialog_new(
        inscriptio, graphica->fenestra_principalis, GTK_FILE_CHOOSER_ACTION_OPEN,
        "REVOCA", GTK_RESPONSE_CANCEL, "APERI", GTK_RESPONSE_ACCEPT, NULL);
    if (editor->via[0]) graphica->api.gtk_file_chooser_set_filename(dialogum, editor->via);
    int responsum = graphica->api.gtk_dialog_run(dialogum);
    int recte = 0;
    if (responsum == GTK_RESPONSE_ACCEPT) {
        char *via = graphica->api.gtk_file_chooser_get_filename(dialogum);
        if (via) {
            recte = editor_archivum_onera(graphica, editor, titulus, via, 1);
            graphica->api.g_free(via);
        }
    }
    graphica->api.gtk_widget_destroy(dialogum);
    return recte;
}

static int editor_serva(Graphica *graphica, Elementum *editor, Elementum *titulus,
                        const char *inscriptio, const char *nomen_initiale) {
    char via_electa[PATH_MAX];
    via_electa[0] = '\0';
    if (editor->via[0]) {
        snprintf(via_electa, sizeof via_electa, "%s", editor->via);
    } else {
        GtkWidget *dialogum = graphica->api.gtk_file_chooser_dialog_new(
            inscriptio, graphica->fenestra_principalis, GTK_FILE_CHOOSER_ACTION_SAVE,
            "REVOCA", GTK_RESPONSE_CANCEL, "SERVA", GTK_RESPONSE_ACCEPT, NULL);
        graphica->api.gtk_file_chooser_set_current_name(dialogum, nomen_initiale);
        int responsum = graphica->api.gtk_dialog_run(dialogum);
        if (responsum == GTK_RESPONSE_ACCEPT) {
            char *via = graphica->api.gtk_file_chooser_get_filename(dialogum);
            if (via) {
                snprintf(via_electa, sizeof via_electa, "%s", via);
                graphica->api.g_free(via);
            }
        }
        graphica->api.gtk_widget_destroy(dialogum);
    }
    if (!via_electa[0]) return 0;
    char *textus = textus_elementi(graphica, editor);
    if (!textus) return 0;
    int recte = scribe_archivum(via_electa, textus, strlen(textus));
    graphica->api.g_free(textus);
    if (recte) {
        snprintf(editor->via, sizeof editor->via, "%s", via_electa);
        titulum_viae_pone(graphica, titulus, via_electa);
    }
    return recte;
}

static void actionem_applica(Graphica *graphica, Actio *actio) {
    Elementum *destinatio = elementum_inveni(graphica, actio->destinatio);
    Elementum *auxilium = actio->auxilium[0] ? elementum_inveni(graphica, actio->auxilium) : NULL;
    char *textus = NULL;
    size_t n = 0;
    switch (actio->genus) {
        case ACTIO_TEXTUS:
            if (destinatio) textum_elemento_pone(graphica, destinatio, actio->textus);
            break;
        case ACTIO_TEXTUS_ARCHIVO:
            if (destinatio && lege_archivum(actio->via, &textus, &n)) {
                (void)n;
                textum_elemento_pone(graphica, destinatio, textus);
                free(textus);
            }
            break;
        case ACTIO_SENSIBILIS:
            if (destinatio) graphica->api.gtk_widget_set_sensitive(destinatio->widget, actio->numerus != 0);
            break;
        case ACTIO_NOVUM:
            if (destinatio && lege_archivum(actio->via, &textus, &n)) {
                (void)n;
                textum_elemento_pone(graphica, destinatio, textus);
                free(textus);
                destinatio->via[0] = '\0';
                titulum_viae_pone(graphica, auxilium, NULL);
                exporta_valores(graphica);
            }
            break;
        case ACTIO_APERI:
            if (destinatio) dialogum_aperi(graphica, destinatio, auxilium, actio->textus);
            break;
        case ACTIO_SERVA:
            if (destinatio) editor_serva(graphica, destinatio, auxilium, actio->textus, actio->via);
            break;
        case ACTIO_TITULUS_FENESTRAE:
            if (destinatio) graphica->api.gtk_window_set_title(destinatio->widget, actio->textus);
            break;
        case ACTIO_CLAUDE:
            graphica->api.gtk_main_quit();
            break;
    }
}

static int responsa_vindex_lege(void *datum) {
    Graphica *graphica = datum;
    unsigned char responsa[64];
    ssize_t n = read(graphica->canalis_ab_vindex, responsa, sizeof responsa);
    if (n < 0 && (errno == EAGAIN || errno == EWOULDBLOCK || errno == EINTR)) return 1;
    if (n <= 0) return 1;
    for (ssize_t i = 0; i < n; ++i) {
        for (size_t j = 0; j < graphica->numerus_actionum; ++j) {
            if (graphica->actiones[j].responsum == responsa[i])
                actionem_applica(graphica, &graphica->actiones[j]);
        }
    }
    return 1;
}

static int orientationem(const char *textus) {
    return strcmp(textus, "HORIZONTALIS") == 0 ? GTK_ORIENTATION_HORIZONTAL : GTK_ORIENTATION_VERTICAL;
}

static int stilum_applica(Graphica *graphica, const char *species) {
    char via[PATH_MAX];
    if (!viam_resolve(graphica, species, via, sizeof via)) return 0;
    char *css = NULL;
    size_t n = 0;
    if (!lege_archivum(via, &css, &n)) return 0;
    GtkCssProvider *provider = graphica->api.gtk_css_provider_new();
    if (!provider) { free(css); return 0; }
    int recte = graphica->api.gtk_css_provider_load_from_data(provider, css, (long)n, NULL);
    free(css);
    if (recte) {
        GdkScreen *screen = graphica->api.gdk_screen_get_default();
        if (screen) graphica->api.gtk_style_context_add_provider_for_screen(
            screen, provider, GTK_STYLE_PROVIDER_PRIORITY_APPLICATION);
    }
    graphica->api.g_object_unref(provider);
    return recte;
}

static int actionem_describe(Graphica *graphica, char **campi, size_t n) {
    int codex = 0;
    if (n < 4 || !numerum(campi[1], &codex) || codex < 1 || codex > 255 ||
        graphica->numerus_actionum >= MAX_ACTIONES) return 0;
    Actio *actio = &graphica->actiones[graphica->numerus_actionum];
    memset(actio, 0, sizeof *actio);
    actio->responsum = (unsigned char)codex;
    if (strcmp(campi[2], "TEXTUS") == 0 && n >= 5) {
        actio->genus = ACTIO_TEXTUS;
        snprintf(actio->destinatio, sizeof actio->destinatio, "%s", campi[3]);
        textum_explica(campi[4], actio->textus, sizeof actio->textus);
    } else if (strcmp(campi[2], "TEXTUS_ARCHIVO") == 0 && n >= 5) {
        actio->genus = ACTIO_TEXTUS_ARCHIVO;
        snprintf(actio->destinatio, sizeof actio->destinatio, "%s", campi[3]);
        if (!viam_resolve(graphica, campi[4], actio->via, sizeof actio->via)) return 0;
    } else if (strcmp(campi[2], "SENSIBILIS") == 0 && n >= 5) {
        actio->genus = ACTIO_SENSIBILIS;
        snprintf(actio->destinatio, sizeof actio->destinatio, "%s", campi[3]);
        if (!numerum(campi[4], &actio->numerus)) return 0;
    } else if (strcmp(campi[2], "NOVUM") == 0 && n >= 6) {
        actio->genus = ACTIO_NOVUM;
        snprintf(actio->destinatio, sizeof actio->destinatio, "%s", campi[3]);
        snprintf(actio->auxilium, sizeof actio->auxilium, "%s", campi[4]);
        if (!viam_resolve(graphica, campi[5], actio->via, sizeof actio->via)) return 0;
    } else if (strcmp(campi[2], "APERI") == 0 && n >= 6) {
        actio->genus = ACTIO_APERI;
        snprintf(actio->destinatio, sizeof actio->destinatio, "%s", campi[3]);
        snprintf(actio->auxilium, sizeof actio->auxilium, "%s", campi[4]);
        textum_explica(campi[5], actio->textus, sizeof actio->textus);
    } else if (strcmp(campi[2], "SERVA") == 0 && n >= 7) {
        actio->genus = ACTIO_SERVA;
        snprintf(actio->destinatio, sizeof actio->destinatio, "%s", campi[3]);
        snprintf(actio->auxilium, sizeof actio->auxilium, "%s", campi[4]);
        textum_explica(campi[5], actio->textus, sizeof actio->textus);
        snprintf(actio->via, sizeof actio->via, "%s", campi[6]);
    } else if (strcmp(campi[2], "TITULUS_FENESTRAE") == 0 && n >= 5) {
        actio->genus = ACTIO_TITULUS_FENESTRAE;
        snprintf(actio->destinatio, sizeof actio->destinatio, "%s", campi[3]);
        textum_explica(campi[4], actio->textus, sizeof actio->textus);
    } else if (strcmp(campi[2], "CLAUDE") == 0) {
        actio->genus = ACTIO_CLAUDE;
    } else return 0;
    graphica->numerus_actionum++;
    return 1;
}

static int formam_construe(Graphica *graphica, const char *via_formae) {
    char *forma = NULL;
    size_t magnitudo = 0;
    if (!directoria_formae_pone(graphica, via_formae) ||
        !lege_archivum(via_formae, &forma, &magnitudo)) return 0;
    (void)magnitudo;
    size_t linea_n = 0;
    char *cursor = forma;
    while (cursor && *cursor) {
        char *finis = strchr(cursor, '\n');
        if (finis) *finis = '\0';
        ++linea_n;
        if (cursor[0] && cursor[0] != '#') {
            char *campi[MAX_CAMPI] = {0};
            size_t n = disseca(cursor, campi, MAX_CAMPI);
            int recte = 0;
            int a = 0, b = 0, c = 0;

            if (strcmp(campi[0], "FENESTRA") == 0 && n >= 6 &&
                numerum(campi[3], &a) && numerum(campi[4], &b) && numerum(campi[5], &c)) {
                Elementum *elementum = elementum_crea(graphica, campi[1], GENUS_FENESTRA);
                if (elementum) {
                    elementum->widget = graphica->api.gtk_window_new(GTK_WINDOW_TOPLEVEL);
                    elementum->internum = elementum->widget;
                    graphica->api.gtk_window_set_title(elementum->widget, campi[2]);
                    graphica->api.gtk_window_set_default_size(elementum->widget, a, b);
                    graphica->api.gtk_container_set_border_width(elementum->widget,
                                                                  (unsigned int)(c < 0 ? 0 : c));
                    graphica->api.gtk_widget_set_name(elementum->widget, elementum->id);
                    graphica->api.g_signal_connect_data(elementum->widget, "destroy",
                        (void (*)(void))cum_claude, graphica, NULL, 0);
                    if (!graphica->fenestra_principalis) graphica->fenestra_principalis = elementum->widget;
                    recte = 1;
                }
            } else if ((strcmp(campi[0], "VERTICALIS") == 0 ||
                        strcmp(campi[0], "HORIZONTALIS") == 0) &&
                       n >= 6 && numerum(campi[3], &a) && numerum(campi[5], &b)) {
                GenusElementi genus = strcmp(campi[0], "VERTICALIS") == 0
                    ? GENUS_VERTICALIS : GENUS_HORIZONTALIS;
                Elementum *elementum = elementum_crea(graphica, campi[1], genus);
                if (elementum) {
                    elementum->widget = graphica->api.gtk_box_new(
                        genus == GENUS_VERTICALIS ? GTK_ORIENTATION_VERTICAL : GTK_ORIENTATION_HORIZONTAL, a);
                    elementum->internum = elementum->widget;
                    graphica->api.gtk_widget_set_name(elementum->widget, elementum->id);
                    recte = applica_parenti(graphica, elementum, campi[2], campi[4], b);
                }
            } else if (strcmp(campi[0], "TITULUS") == 0 && n >= 7 && numerum(campi[6], &a)) {
                Elementum *elementum = elementum_crea(graphica, campi[1], GENUS_TITULUS);
                if (elementum) {
                    char textus[1024];
                    textum_explica(campi[3], textus, sizeof textus);
                    elementum->widget = graphica->api.gtk_label_new(textus);
                    elementum->internum = elementum->widget;
                    float align = strcmp(campi[4], "FINIS") == 0 ? 1.0f :
                                  (strcmp(campi[4], "MEDIUM") == 0 ? 0.5f : 0.0f);
                    graphica->api.gtk_label_set_xalign(elementum->widget, align);
                    graphica->api.gtk_widget_set_name(elementum->widget, elementum->id);
                    recte = applica_parenti(graphica, elementum, campi[2], campi[5], a);
                }
            } else if (strcmp(campi[0], "BULLA") == 0 && n >= 8 &&
                       numerum(campi[4], &a) && numerum(campi[7], &b) && a > 0 && a < 256) {
                Elementum *elementum = elementum_crea(graphica, campi[1], GENUS_BULLA);
                if (elementum) {
                    char textus[1024], auxilium[1024];
                    textum_explica(campi[3], textus, sizeof textus);
                    textum_explica(campi[5], auxilium, sizeof auxilium);
                    elementum->widget = graphica->api.gtk_button_new_with_label(textus);
                    elementum->internum = elementum->widget;
                    elementum->eventum = a;
                    graphica->api.gtk_widget_set_name(elementum->widget, elementum->id);
                    if (auxilium[0]) graphica->api.gtk_widget_set_tooltip_text(elementum->widget, auxilium);
                    graphica->api.g_signal_connect_data(elementum->widget, "clicked",
                        (void (*)(void))cum_bulla, elementum, NULL, 0);
                    recte = applica_parenti(graphica, elementum, campi[2], campi[6], b);
                }
            } else if (strcmp(campi[0], "EDITOR") == 0 && n >= 7 && numerum(campi[6], &a)) {
                Elementum *elementum = elementum_crea(graphica, campi[1], GENUS_EDITOR);
                if (elementum) {
                    elementum->widget = graphica->api.gtk_scrolled_window_new(NULL, NULL);
                    graphica->api.gtk_scrolled_window_set_policy(elementum->widget,
                                                                  GTK_POLICY_AUTOMATIC, GTK_POLICY_AUTOMATIC);
                    elementum->internum = graphica->api.gtk_text_view_new();
                    elementum->receptaculum = graphica->api.gtk_text_view_get_buffer(elementum->internum);
                    graphica->api.gtk_text_view_set_monospace(elementum->internum, 1);
                    graphica->api.gtk_text_view_set_wrap_mode(elementum->internum, GTK_WRAP_NONE);
                    graphica->api.gtk_text_view_set_left_margin(elementum->internum, 16);
                    graphica->api.gtk_text_view_set_right_margin(elementum->internum, 16);
                    graphica->api.gtk_text_view_set_top_margin(elementum->internum, 12);
                    graphica->api.gtk_text_view_set_bottom_margin(elementum->internum, 12);
                    graphica->api.gtk_widget_set_name(elementum->internum, elementum->id);
                    graphica->api.gtk_container_add(elementum->widget, elementum->internum);
                    const char *species = campi[3];
                    char via[PATH_MAX] = {0};
                    int retine = 0;
                    if (strncmp(species, "ARGUMENTUM", 10) == 0) {
                        if (graphica->fons_initialis && graphica->fons_initialis[0]) {
                            snprintf(via, sizeof via, "%s", graphica->fons_initialis);
                            retine = 1;
                        } else if (species[10] == ':') {
                            viam_resolve(graphica, species + 11, via, sizeof via);
                        }
                    } else viam_resolve(graphica, species, via, sizeof via);
                    Elementum *titulus = strcmp(campi[4], "-") == 0 ? NULL : elementum_inveni(graphica, campi[4]);
                    if (via[0] && !editor_archivum_onera(graphica, elementum, titulus, via, retine)) {
                        nuntia("ERRATUM: fons initialis legi non potest: %s\n", via);
                    }
                    recte = applica_parenti(graphica, elementum, campi[2], campi[5], a);
                }
            } else if (strcmp(campi[0], "EXITUS") == 0 && n >= 7 &&
                       numerum(campi[4], &a) && numerum(campi[6], &b)) {
                Elementum *elementum = elementum_crea(graphica, campi[1], GENUS_EXITUS);
                if (elementum) {
                    elementum->widget = graphica->api.gtk_scrolled_window_new(NULL, NULL);
                    graphica->api.gtk_scrolled_window_set_policy(elementum->widget,
                                                                  GTK_POLICY_AUTOMATIC, GTK_POLICY_AUTOMATIC);
                    elementum->internum = graphica->api.gtk_text_view_new();
                    elementum->receptaculum = graphica->api.gtk_text_view_get_buffer(elementum->internum);
                    graphica->api.gtk_text_view_set_monospace(elementum->internum, 1);
                    graphica->api.gtk_text_view_set_editable(elementum->internum, 0);
                    graphica->api.gtk_text_view_set_left_margin(elementum->internum, 12);
                    graphica->api.gtk_text_view_set_right_margin(elementum->internum, 12);
                    graphica->api.gtk_text_view_set_top_margin(elementum->internum, 8);
                    graphica->api.gtk_text_view_set_bottom_margin(elementum->internum, 8);
                    graphica->api.gtk_widget_set_name(elementum->internum, elementum->id);
                    graphica->api.gtk_container_add(elementum->widget, elementum->internum);
                    char textus[1024];
                    textum_explica(campi[3], textus, sizeof textus);
                    textum_elemento_pone(graphica, elementum, textus);
                    graphica->api.gtk_widget_set_size_request(elementum->widget, -1, a);
                    recte = applica_parenti(graphica, elementum, campi[2], campi[5], b);
                }
            } else if (strcmp(campi[0], "CAMPUS_TEXTUS") == 0 && n >= 7 && numerum(campi[6], &a)) {
                Elementum *elementum = elementum_crea(graphica, campi[1], GENUS_CAMPUS_TEXTUS);
                if (elementum) {
                    char textus[1024], locus[1024];
                    textum_explica(campi[3], textus, sizeof textus);
                    textum_explica(campi[4], locus, sizeof locus);
                    elementum->widget = graphica->api.gtk_entry_new();
                    elementum->internum = elementum->widget;
                    graphica->api.gtk_entry_set_text(elementum->widget, textus);
                    graphica->api.gtk_entry_set_placeholder_text(elementum->widget, locus);
                    graphica->api.gtk_widget_set_name(elementum->widget, elementum->id);
                    recte = applica_parenti(graphica, elementum, campi[2], campi[5], a);
                }
            } else if (strcmp(campi[0], "DIVISOR") == 0 && n >= 7 &&
                       numerum(campi[4], &a) && numerum(campi[6], &b)) {
                Elementum *elementum = elementum_crea(graphica, campi[1], GENUS_DIVISOR);
                if (elementum) {
                    elementum->widget = graphica->api.gtk_paned_new(orientationem(campi[3]));
                    elementum->internum = elementum->widget;
                    graphica->api.gtk_paned_set_position(elementum->widget, a);
                    graphica->api.gtk_widget_set_name(elementum->widget, elementum->id);
                    recte = applica_parenti(graphica, elementum, campi[2], campi[5], b);
                }
            } else if (strcmp(campi[0], "SEPARATOR") == 0 && n >= 6 && numerum(campi[5], &a)) {
                Elementum *elementum = elementum_crea(graphica, campi[1], GENUS_SEPARATOR);
                if (elementum) {
                    elementum->widget = graphica->api.gtk_separator_new(orientationem(campi[3]));
                    elementum->internum = elementum->widget;
                    graphica->api.gtk_widget_set_name(elementum->widget, elementum->id);
                    recte = applica_parenti(graphica, elementum, campi[2], campi[4], a);
                }
            } else if (strcmp(campi[0], "STILUS") == 0 && n >= 2) {
                recte = stilum_applica(graphica, campi[1]);
            } else if (strcmp(campi[0], "ICONA") == 0 && n >= 3) {
                Elementum *fenestra = elementum_inveni(graphica, campi[1]);
                char via[PATH_MAX];
                if (fenestra && viam_resolve(graphica, campi[2], via, sizeof via)) {
                    graphica->api.gtk_window_set_icon_from_file(fenestra->widget, via, NULL);
                    recte = 1;
                }
            } else if (strcmp(campi[0], "EVENTUM_CLAUSURAE") == 0 && n >= 2 &&
                       numerum(campi[1], &a) && a > 0 && a < 256) {
                graphica->eventum_clausurae = (unsigned char)a;
                recte = 1;
            } else if (strcmp(campi[0], "CLAVIS") == 0 && n >= 3 &&
                       numerum(campi[2], &a) && a > 0 && a < 256) {
                Elementum *elementum = elementum_inveni(graphica, campi[1]);
                if (elementum && elementum->internum) {
                    elementum->eventum_clavis = a;
                    graphica->api.g_signal_connect_data(elementum->internum, "key-release-event",
                        (void (*)(void))cum_clavis, elementum, NULL, 0);
                    recte = 1;
                }
            } else if (strcmp(campi[0], "MUS") == 0 && n >= 3 &&
                       numerum(campi[2], &a) && a > 0 && a < 256) {
                Elementum *elementum = elementum_inveni(graphica, campi[1]);
                if (elementum && elementum->internum) {
                    elementum->eventum_muris = a;
                    graphica->api.gtk_widget_add_events(elementum->internum, 1 << 8);
                    graphica->api.g_signal_connect_data(elementum->internum, "button-press-event",
                        (void (*)(void))cum_mure, elementum, NULL, 0);
                    recte = 1;
                }
            } else if (strcmp(campi[0], "MUTATIO") == 0 && n >= 3 &&
                       numerum(campi[2], &a) && a > 0 && a < 256) {
                Elementum *elementum = elementum_inveni(graphica, campi[1]);
                if (elementum && (elementum->genus == GENUS_EDITOR ||
                                  elementum->genus == GENUS_CAMPUS_TEXTUS)) {
                    elementum->eventum_mutationis = a;
                    void *signifer = elementum->genus == GENUS_EDITOR
                        ? (void *)elementum->receptaculum : (void *)elementum->internum;
                    graphica->api.g_signal_connect_data(signifer, "changed",
                        (void (*)(void))cum_mutatione, elementum, NULL, 0);
                    recte = 1;
                }
            } else if (strcmp(campi[0], "RESPONSUM") == 0) {
                recte = actionem_describe(graphica, campi, n);
            }
            if (!recte) {
                nuntia("ERRATUM: forma invalida in linea %zu.\n", linea_n);
                free(forma);
                return 0;
            }
        }
        cursor = finis ? finis + 1 : NULL;
    }
    free(forma);
    if (!graphica->fenestra_principalis) return 0;
    exporta_valores(graphica);
    graphica->api.gtk_widget_show_all(graphica->fenestra_principalis);
    return 1;
}

static int forma_valida(const char *via_formae) {
    char *forma = NULL;
    size_t magnitudo = 0;
    if (!lege_archivum(via_formae, &forma, &magnitudo)) return 0;
    (void)magnitudo;
    static const char *directivae[] = {
        "FENESTRA", "VERTICALIS", "HORIZONTALIS", "TITULUS", "BULLA",
        "EDITOR", "EXITUS", "CAMPUS_TEXTUS", "DIVISOR", "SEPARATOR",
        "STILUS", "ICONA", "EVENTUM_CLAUSURAE", "CLAVIS", "MUS", "MUTATIO", "RESPONSUM"
    };
    size_t minima[] = {6, 6, 6, 7, 8, 7, 7, 7, 7, 6, 2, 3, 2, 3, 3, 3, 4};
    size_t linea_n = 0;
    int fenestra = 0;
    char *cursor = forma;
    while (cursor && *cursor) {
        char *finis = strchr(cursor, '\n');
        if (finis) *finis = '\0';
        ++linea_n;
        if (cursor[0] && cursor[0] != '#') {
            char *campi[MAX_CAMPI] = {0};
            size_t n = disseca(cursor, campi, MAX_CAMPI);
            int cognita = 0;
            for (size_t i = 0; i < sizeof directivae / sizeof directivae[0]; ++i) {
                if (strcmp(campi[0], directivae[i]) == 0) {
                    cognita = n >= minima[i];
                    break;
                }
            }
            if (!cognita) {
                nuntia("ERRATUM: directiva formae invalida in linea %zu.\n", linea_n);
                free(forma);
                return 0;
            }
            if (strcmp(campi[0], "FENESTRA") == 0) fenestra = 1;
        }
        cursor = finis ? finis + 1 : NULL;
    }
    free(forma);
    return fenestra;
}

static int canalis_remove_si_fifo(const char *via) {
    struct stat status;
    if (lstat(via, &status) != 0) return errno == ENOENT;
    if (!S_ISFIFO(status.st_mode)) {
        nuntia("ERRATUM: via canalis iam ab alio archivo tenetur: %s\n", via);
        return 0;
    }
    return unlink(via) == 0;
}

static int canales_praepara(Graphica *graphica) {
    if (!canalis_remove_si_fifo(CANALIS_AD_VINDEX) ||
        !canalis_remove_si_fifo(CANALIS_AB_VINDEX)) return 0;
    if (mkfifo(CANALIS_AD_VINDEX, 0600) != 0) return 0;
    if (mkfifo(CANALIS_AB_VINDEX, 0600) != 0) {
        unlink(CANALIS_AD_VINDEX);
        return 0;
    }
    graphica->canalis_ad_vindex = open(CANALIS_AD_VINDEX, O_RDWR | O_NONBLOCK);
    graphica->canalis_ab_vindex = open(CANALIS_AB_VINDEX, O_RDWR | O_NONBLOCK);
    if (graphica->canalis_ad_vindex < 0 || graphica->canalis_ab_vindex < 0) {
        if (graphica->canalis_ad_vindex >= 0) close(graphica->canalis_ad_vindex);
        if (graphica->canalis_ab_vindex >= 0) close(graphica->canalis_ab_vindex);
        unlink(CANALIS_AD_VINDEX);
        unlink(CANALIS_AB_VINDEX);
        return 0;
    }
    return 1;
}

static void canales_purga(Graphica *graphica) {
    if (graphica->canalis_ad_vindex >= 0) close(graphica->canalis_ad_vindex);
    if (graphica->canalis_ab_vindex >= 0) close(graphica->canalis_ab_vindex);
    unlink(CANALIS_AD_VINDEX);
    unlink(CANALIS_AB_VINDEX);
}

static void paratum_signa(int descriptor, unsigned char status) {
    if (descriptor < 0) return;
    while (write(descriptor, &status, 1) < 0 && errno == EINTR) {}
    close(descriptor);
}

int main(int argc, char **argv) {
    Graphica graphica;
    memset(&graphica, 0, sizeof graphica);
    graphica.canalis_ad_vindex = -1;
    graphica.canalis_ab_vindex = -1;
    graphica.eventum_clausurae = 81;

    if (argc >= 3 && strcmp(argv[1], "--verifica-formam") == 0) {
        if (!forma_valida(argv[2])) return 65;
        puts("RECTE: forma graphica valida est");
        return 0;
    }
    if (!onera_gtk(&graphica)) return 69;
    if (argc >= 2 && strcmp(argv[1], "--probatio") == 0) {
        puts("RECTE: pons GTK declarativus integer est");
        claude_gtk(&graphica);
        return 0;
    }

    int modus_servitoris = argc >= 3 && strcmp(argv[1], "--servitor") == 0;
    int descriptor_parati = -1;
    if (modus_servitoris) {
        int tubus_parati[2];
        if (pipe(tubus_parati) != 0) return 69;
        pid_t filius = fork();
        if (filius < 0) return 69;
        if (filius > 0) {
            close(tubus_parati[1]);
            unsigned char status = 69;
            while (read(tubus_parati[0], &status, 1) < 0 && errno == EINTR) {}
            close(tubus_parati[0]);
            claude_gtk(&graphica);
            return status;
        }
        close(tubus_parati[0]);
        descriptor_parati = tubus_parati[1];
        graphica.modus_servitoris = 1;
        graphica.fons_initialis = argc >= 4 ? argv[3] : NULL;
        setsid();
    }

    if (modus_servitoris) {
        if (!canales_praepara(&graphica)) {
            nuntia("ERRATUM: canales graphici creari non possunt.\n");
            paratum_signa(descriptor_parati, 73);
            claude_gtk(&graphica);
            return 73;
        }
        if (!graphica.api.gtk_init_check(&argc, &argv)) {
            nuntia("ERRATUM: sessio graphica GTK aperiri non potest.\n");
            paratum_signa(descriptor_parati, 69);
            canales_purga(&graphica);
            claude_gtk(&graphica);
            return 69;
        }
        if (!formam_construe(&graphica, argv[2])) {
            paratum_signa(descriptor_parati, 65);
            canales_purga(&graphica);
            claude_gtk(&graphica);
            return 65;
        }
        graphica.api.g_timeout_add(80, responsa_vindex_lege, &graphica);
        paratum_signa(descriptor_parati, 0);
        graphica.api.gtk_main();
        canales_purga(&graphica);
        claude_gtk(&graphica);
        return 0;
    }

    nuntia("USUS: vindex_graphica --servitor forma.graphica [fons.vindex]\n");
    claude_gtk(&graphica);
    return 64;
}
