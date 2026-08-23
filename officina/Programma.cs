using System.Windows.Forms;

namespace Vindex.Officina;

internal static class Programma
{
    [STAThread]
    private static int Main(string[] argumenta)
    {
        if (argumenta.Length >= 1 && argumenta[0] == "--probatio")
        {
            return Probationes.Exsequere();
        }

        if (argumenta.Length >= 3 && argumenta[0] == "--proba-proiectum")
        {
            return Probationes.ProbaProiectumAsync(argumenta[1], argumenta[2])
                .GetAwaiter().GetResult();
        }

        ApplicationConfiguration.Initialize();
        ConfiguratioOfficinae configuratio = ConfiguratioOfficinae.Lege(AppContext.BaseDirectory);
        string? manifestum = argumenta.FirstOrDefault(via =>
            via.EndsWith(".vindex", StringComparison.OrdinalIgnoreCase));
        Application.Run(new FenestraOfficinae(configuratio, manifestum));
        return 0;
    }
}
