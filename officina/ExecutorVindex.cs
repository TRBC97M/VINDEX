using System.Diagnostics;
using System.Text;

namespace Vindex.Officina;

internal sealed record ResultatumProcessus(int Status, string Exitus, string Errata);

internal static class ExecutorVindex
{
    public static Task<ResultatumProcessus> ConstrueAsync(
        string compilator,
        ProiectumVindex proiectum,
        CancellationToken signum = default)
        => CurrereAsync(
            compilator,
            new[] { "PROIECTUM", proiectum.ViaManifesti },
            proiectum.Radix,
            signum);

    public static Task<ResultatumProcessus> ExsequereAsync(
        ProiectumVindex proiectum,
        CancellationToken signum = default)
        => CurrereAsync(proiectum.ViaProducti, Array.Empty<string>(), proiectum.Radix, signum);

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
