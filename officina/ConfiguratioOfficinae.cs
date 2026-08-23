using System.Drawing;
using System.Text.RegularExpressions;

namespace Vindex.Officina;

internal sealed class ConfiguratioOfficinae
{
    private readonly Dictionary<string, string> _valores = new(StringComparer.OrdinalIgnoreCase);

    public string Titulus => Valor("TITULUS_FENESTRAE", "VINDEX // OFFICINA");
    public string Subtitulus => Valor("SUBTITULUS", "AMBITUS PROGRAMMATIONIS");
    public int Latitudo => Numerus("LATITUDO", 1440);
    public int Altitudo => Numerus("ALTITUDO", 900);

    public static ConfiguratioOfficinae Lege(string radix)
    {
        ConfiguratioOfficinae configuratio = new();
        configuratio.LegeArchivum(Path.Combine(radix, "formae", "officina.forma"));
        configuratio.LegeArchivum(Path.Combine(radix, "formae", "officina.stilus"));
        return configuratio;
    }

    public string Valor(string nomen, string praedefinitum)
        => _valores.TryGetValue(nomen, out string? valor) ? valor : praedefinitum;

    public Color Color(string nomen, string praedefinitus)
    {
        string valor = Valor(nomen, praedefinitus);
        try
        {
            return ColorTranslator.FromHtml(valor);
        }
        catch
        {
            return ColorTranslator.FromHtml(praedefinitus);
        }
    }

    private int Numerus(string nomen, int praedefinitus)
        => _valores.TryGetValue(nomen, out string? valor) && int.TryParse(valor, out int numerus)
            ? numerus
            : praedefinitus;

    private void LegeArchivum(string via)
    {
        if (!File.Exists(via))
        {
            return;
        }

        foreach (string lineaBruta in File.ReadLines(via))
        {
            string linea = lineaBruta.Trim();
            if (linea.Length == 0 || linea.StartsWith("//", StringComparison.Ordinal))
            {
                continue;
            }

            Match citatum = Regex.Match(linea, "^(?<nomen>[A-Z_]+)\\s+\"(?<valor>.*)\"\\.$");
            if (citatum.Success)
            {
                _valores[citatum.Groups["nomen"].Value] = citatum.Groups["valor"].Value;
                continue;
            }

            Match simplex = Regex.Match(linea, "^(?<nomen>[A-Z_]+)\\s+(?<valor>[^.]+)\\.$");
            if (simplex.Success)
            {
                _valores[simplex.Groups["nomen"].Value] = simplex.Groups["valor"].Value.Trim();
            }
        }
    }
}
