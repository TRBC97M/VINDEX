using System.Text.RegularExpressions;

namespace Vindex.Officina;

internal sealed record DiagnosticumVindex(string Via, int Linea, int Columna, string Nuntius)
{
    private static readonly Regex FormaDiagnostici = new(
        @"DIAGNOSTICUM VINDEX\r?\n" +
        @"FONS\r?\n(?<fons>[^\r\n]+)\r?\n" +
        @"LINEA\r?\n(?<linea>\d+)\r?\n" +
        @"COLUMNA\r?\n(?<columna>\d+)\r?\n" +
        @"NUNTIUS\r?\n(?<nuntius>[^\r\n]+)",
        RegexOptions.CultureInvariant);

    public static IReadOnlyList<DiagnosticumVindex> Extrahe(string textus)
    {
        List<DiagnosticumVindex> diagnostica = [];
        foreach (Match pars in FormaDiagnostici.Matches(textus))
        {
            diagnostica.Add(new DiagnosticumVindex(
                pars.Groups["fons"].Value,
                int.Parse(pars.Groups["linea"].Value),
                int.Parse(pars.Groups["columna"].Value),
                pars.Groups["nuntius"].Value));
        }
        return diagnostica;
    }
}
