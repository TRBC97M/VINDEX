using System.Text;

namespace Vindex.Officina;

internal static class FabricaProiectiVindex
{
    private const string NomenFontis = "principalis.vindex";
    private const string NomenManifesti = "proiectum.vindex";
    private const string NomenProducti = "programma.exe";

    public static ProiectumVindex Crea(string radix)
    {
        if (string.IsNullOrWhiteSpace(radix))
        {
            throw new ArgumentException("Directorium novi proiecti deest.", nameof(radix));
        }

        string directorium = Path.GetFullPath(radix);
        Directory.CreateDirectory(directorium);

        string viaFontis = Path.Combine(directorium, NomenFontis);
        string viaManifesti = Path.Combine(directorium, NomenManifesti);
        string viaProducti = Path.Combine(directorium, NomenProducti);
        if (File.Exists(viaFontis) || File.Exists(viaManifesti) || File.Exists(viaProducti))
        {
            throw new InvalidOperationException("Directorium iam proiectum VINDEX aut productum canonicum continet; nihil rescribitur.");
        }

        UTF8Encoding utf8 = new(false);
        string fons =
            "FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n" +
            "    PROCLAMA \"Salve, VINDEX!\".\n" +
            "    REDDE 0.\n" +
            "FIN-FUNCTIO.\n";
        string manifestum =
            "PROIECTUM VINDEX.\n" +
            $"FONS \"{NomenFontis}\".\n" +
            $"PRODUCTUM \"{NomenProducti}\".\n" +
            "DESTINATIO PE.\n" +
            "FIN-PROIECTUM.\n";

        File.WriteAllText(viaFontis, fons, utf8);
        try
        {
            File.WriteAllText(viaManifesti, manifestum, utf8);
        }
        catch
        {
            File.Delete(viaFontis);
            throw;
        }

        return ProiectumVindex.Lege(viaManifesti);
    }
}
