using System.Diagnostics;
using System.Text;
using System.Text.RegularExpressions;

namespace Vindex.Officina;

internal sealed record ResultatumProcessus(int Status, string Exitus, string Errata);

internal static class ExecutorVindex
{
    private static readonly Regex FonsDiagnosticusVacuus = new(
        @"DIAGNOSTICUM VINDEX\r?\nFONS\r?\n(?=\r?\nLINEA\r?\n)",
        RegexOptions.CultureInvariant);

    public static async Task<ResultatumProcessus> ConstrueAsync(
        string compilator,
        ProiectumVindex proiectum,
        CancellationToken signum = default)
    {
        ResultatumProcessus resultatum = await CurrereAsync(
            compilator,
            new[] { "PROIECTUM", proiectum.ViaManifesti },
            proiectum.Radix,
            signum);

        // Compilator Win64 canonicus hodiernus R2 locum et nuntium recte
        // reddit, sed in hoc itinere interdum FONS vacuum relinquit. Officina
        // fontem non divinat: eum ex manifesto iam lecto complet, donec
        // regressio compilatoris ipsa separatim corrigatur.
        return resultatum with
        {
            Exitus = CompleFontemDiagnosticorum(resultatum.Exitus, proiectum.ViaFontis),
            Errata = CompleFontemDiagnosticorum(resultatum.Errata, proiectum.ViaFontis),
        };
    }

    public static Task<ResultatumProcessus> ExsequereAsync(
        ProiectumVindex proiectum,
        CancellationToken signum = default)
        => CurrereAsync(proiectum.ViaProducti, Array.Empty<string>(), proiectum.Radix, signum);

    private static string CompleFontemDiagnosticorum(string textus, string viaFontis)
        => FonsDiagnosticusVacuus.Replace(
            textus,
            compositio => compositio.Value + viaFontis);

    private static async Task<ResultatumProcessus> CurrereAsync(
        string via,
        IEnumerable<string> argumenta,
        string directorium,
        CancellationToken signum)
    {
        ProcessStartInfo initium = new()
        {
            FileName = via,
            WorkingDirectory = directorium,
            UseShellExecute = false,
            CreateNoWindow = true,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            StandardOutputEncoding = Encoding.UTF8,
            StandardErrorEncoding = Encoding.UTF8,
        };
        foreach (string argumentum in argumenta)
        {
            initium.ArgumentList.Add(argumentum);
        }

        using Process processus = new() { StartInfo = initium };
        if (!processus.Start())
        {
            throw new InvalidOperationException("Processus incipere non potest.");
        }

        Task<string> exitus = processus.StandardOutput.ReadToEndAsync();
        Task<string> errata = processus.StandardError.ReadToEndAsync();
        await processus.WaitForExitAsync(signum);
        return new ResultatumProcessus(processus.ExitCode, await exitus, await errata);
    }
}
