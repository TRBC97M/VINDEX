using System.Text.RegularExpressions;

namespace Vindex.Officina;

internal sealed record ProiectumVindex(
    string ViaManifesti,
    string Radix,
    string ViaFontis,
    string ViaProducti,
    string Destinatio)
{
    private static readonly Regex FormaManifesti = new(
        "\\A\\s*PROIECTUM\\s+VINDEX\\s*\\.\\s*" +
        "FONS\\s+\"(?<fons>[^\"]+)\"\\s*\\.\\s*" +
        "PRODUCTUM\\s+\"(?<productum>[^\"]+)\"\\s*\\.\\s*" +
        "DESTINATIO\\s+(?<destinatio>ELF|PE)\\s*\\.\\s*" +
        "FIN-PROIECTUM\\s*\\.\\s*\\z",
        RegexOptions.CultureInvariant);

    public static ProiectumVindex Lege(string viaManifesti)
    {
        string manifestum = Path.GetFullPath(viaManifesti);
        if (!File.Exists(manifestum))
        {
            throw new InvalidDataException("Manifestum proiecti non inventum est.");
        }

        string textus = File.ReadAllText(manifestum);
        Match partes = FormaManifesti.Match(textus);
        if (!partes.Success)
        {
            throw new InvalidDataException("Manifestum proiecti VINDEX invalidum est.");
        }

        string radix = Path.GetDirectoryName(manifestum)
            ?? throw new InvalidDataException("Directorium proiecti non inventum est.");
        string fons = Resolve(radix, partes.Groups["fons"].Value);
        string productum = Resolve(radix, partes.Groups["productum"].Value);
        return new ProiectumVindex(
            manifestum,
            radix,
            fons,
            productum,
            partes.Groups["destinatio"].Value.ToUpperInvariant());
    }

    private static string Resolve(string radix, string via)
        => Path.GetFullPath(Path.IsPathRooted(via) ? via : Path.Combine(radix, via));
}
