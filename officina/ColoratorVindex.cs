using System.Drawing;
using System.Text.RegularExpressions;
using System.Windows.Forms;

namespace Vindex.Officina;

internal static class ColoratorVindex
{
    private const string Verba =
        "FUNCTIO|FIN-FUNCTIO|PRINCIPALIS|REDDENS|ACCIPIT|DECLARA|SICUT|VALENS|" +
        "NUMERUS|LITTERA|VERITAS|FLUITANS|VACUUM|ACUS|ORDO|CAPACITAS|FORMA|CAMPUS|FIN-FORMA|" +
        "SI|TUNC|ALITER|FIN-SI|DUM|PERFICE|FIN-DUM|PER|AB|AD|FIN-PER|DESINE|" +
        "REDDE|PROCLAMA|IMPORTA|SEDES|CONTENTUM|RESERVA|RESERVA_OCTETA|LIBERA|" +
        "APERI_LEGERE|APERI_SCRIBERE|LEGE|MITTE|CLAUDE|OCTETUS|OCTETUS_AB|SCRIBE_OCTETUM_AB";

    private static readonly Regex VerbaClavia = new($@"\b(?:{Verba})\b", RegexOptions.CultureInvariant);
    private static readonly Regex Numeri = new(@"(?<![\w])(?:-?\d+(?:\.\d+)?)(?![\w])", RegexOptions.CultureInvariant);
    private static readonly Regex Cathenae = new("\"(?:\\.|[^\"\\])*\"", RegexOptions.CultureInvariant);
    private static readonly Regex Commentaria = new(@"//[^\r\n]*", RegexOptions.CultureInvariant);

    public static int NumeraVerbaClavia(string textus) => VerbaClavia.Matches(textus).Count;

    public static void Colora(RichTextBox editor, ConfiguratioOfficinae configuratio)
    {
        int initium = editor.SelectionStart;
        int longitudo = editor.SelectionLength;
        editor.SuspendLayout();
        try
        {
            editor.SelectAll();
            editor.SelectionColor = configuratio.Color("COLOR_TEXTUS", "#D9E6F2");
            Applica(editor, VerbaClavia, configuratio.Color("COLOR_VERBUM", "#7CCBFF"));
            Applica(editor, Numeri, configuratio.Color("COLOR_NUMERI", "#E7C46A"));
            Applica(editor, Cathenae, configuratio.Color("COLOR_CATHENAE", "#9DDAA6"));
            Applica(editor, Commentaria, configuratio.Color("COLOR_COMMENTARII", "#6E8497"));
            editor.Select(Math.Min(initium, editor.TextLength), Math.Min(longitudo, Math.Max(0, editor.TextLength - initium)));
        }
        finally
        {
            editor.ResumeLayout();
        }
    }

    private static void Applica(RichTextBox editor, Regex regula, Color color)
    {
        foreach (Match pars in regula.Matches(editor.Text))
        {
            editor.Select(pars.Index, pars.Length);
            editor.SelectionColor = color;
        }
    }
}
