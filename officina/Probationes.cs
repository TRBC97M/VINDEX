namespace Vindex.Officina;

internal static class Probationes
{
    private static readonly string ViaRelationis = Path.Combine(Path.GetTempPath(), "officina-vindex-probatio.txt");

    public static int Exsequere()
    {
        string radix = Path.Combine(Path.GetTempPath(), "officina-vindex-" + Guid.NewGuid().ToString("N"));
        try
        {
            Directory.CreateDirectory(radix);
            string fons = Path.Combine(radix, "principalis.vindex");
            string manifestum = Path.Combine(radix, "proiectum.vindex");
            File.WriteAllText(fons, "FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n    REDDE 0.\nFIN-FUNCTIO.\n");
            File.WriteAllText(manifestum,
                "PROIECTUM VINDEX.\nFONS \"principalis.vindex\".\nPRODUCTUM \"salve.exe\".\nDESTINATIO PE.\nFIN-PROIECTUM.\n");

            ProiectumVindex proiectum = ProiectumVindex.Lege(manifestum);
            Exige(proiectum.ViaFontis == fons, "Via fontis falsa est.");
            Exige(proiectum.Destinatio == "PE", "Destinatio falsa est.");

            const string relatio = "DIAGNOSTICUM VINDEX\nFONS\nprincipalis.vindex\nLINEA\n2\nCOLUMNA\n5\nNUNTIUS\nERRATUM: instructio ignota est\n";
            IReadOnlyList<DiagnosticumVindex> diagnostica = DiagnosticumVindex.Extrahe(relatio);
            Exige(diagnostica.Count == 1, "Diagnosticum non inventum est.");
            Exige(diagnostica[0].Linea == 2 && diagnostica[0].Columna == 5, "Locus diagnostici falsus est.");
            Exige(ColoratorVindex.NumeraVerbaClavia(File.ReadAllText(fons)) >= 4, "Colorator verba VINDEX non invenit.");
            ConfiguratioOfficinae configuratio = ConfiguratioOfficinae.Lege(AppContext.BaseDirectory);
            Exige(configuratio.Titulus == "VINDEX // OFFICINA", "Forma Officinae non lecta est.");
            using FenestraOfficinae fenestra = new(configuratio, null);
            AmplificatioGradusB.Applica(fenestra, configuratio, _ => { });
            fenestra.CreateControl();
            Exige(fenestra.Text == "VINDEX // OFFICINA" && fenestra.Controls.Count > 0, "Fenestra Officinae non constructa est.");
            Exige(fenestra.Controls.Find("novum", true).Length == 1, "Actio NOVUM PROIECTUM deest.");

            File.WriteAllText(ViaRelationis, "RECTE: probationes Officinae perfectae sunt.\n");
            return 0;
        }
        catch (Exception erratum)
        {
            File.WriteAllText(ViaRelationis, erratum.ToString());
            return 1;
        }
        finally
        {
            if (Directory.Exists(radix))
            {
                Directory.Delete(radix, true);
            }
        }
    }

    public static async Task<int> ProbaProiectumAsync(string compilator, string manifestum)
    {
        try
        {
            ProiectumVindex proiectum = ProiectumVindex.Lege(manifestum);
            ResultatumProcessus compilatio = await ExecutorVindex.ConstrueAsync(compilator, proiectum);
            Exige(compilatio.Status == 0, compilatio.Exitus + compilatio.Errata);
            Exige(File.Exists(proiectum.ViaProducti), "Productum proiecti deest.");
            ResultatumProcessus executio = await ExecutorVindex.ExsequereAsync(proiectum);
            Exige(executio.Status == 0, executio.Exitus + executio.Errata);
            Exige(executio.Exitus.Replace("\r\n", "\n").Trim() == "Salve, VINDEX!", "Exitus proiecti differt.");
            File.WriteAllText(ViaRelationis, "RECTE: proiectum per Officinam constructum et exsecutum est.\n");
            return 0;
        }
        catch (Exception erratum)
        {
            File.WriteAllText(ViaRelationis, erratum.ToString());
            return 1;
        }
    }

    public static async Task<int> ProbaDiagnosticumAsync(string compilator)
    {
        string radix = Path.Combine(Path.GetTempPath(), "officina-vindex-diagnosticum-" + Guid.NewGuid().ToString("N"));
        try
        {
            Directory.CreateDirectory(radix);
            string fons = Path.Combine(radix, "principalis.vindex");
            string manifestum = Path.Combine(radix, "proiectum.vindex");
            File.WriteAllText(fons,
                "FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n" +
                "    IGNOTUM.\n" +
                "    REDDE 0.\n" +
                "FIN-FUNCTIO.\n");
            File.WriteAllText(manifestum,
                "PROIECTUM VINDEX.\nFONS \"principalis.vindex\".\nPRODUCTUM \"erratum.exe\".\nDESTINATIO PE.\nFIN-PROIECTUM.\n");

            ProiectumVindex proiectum = ProiectumVindex.Lege(manifestum);
            ResultatumProcessus compilatio = await ExecutorVindex.ConstrueAsync(compilator, proiectum);
            Exige(compilatio.Status != 0, "Compilatio errata falso successit.");
            string relatio = compilatio.Exitus + "\n" + compilatio.Errata;
            IReadOnlyList<DiagnosticumVindex> diagnostica = DiagnosticumVindex.Extrahe(relatio);
            DiagnosticumVindex? diagnosticum = diagnostica.FirstOrDefault(d =>
                d.Linea == 2 && d.Columna == 5 && d.Nuntius.Contains("instructio ignota", StringComparison.OrdinalIgnoreCase));
            if (diagnosticum is null)
            {
                throw new InvalidOperationException("Diagnosticum reale R2 ab Officina non lectum est.\n" + relatio);
            }
            Exige(Path.GetFileName(diagnosticum.Via).Equals("principalis.vindex", StringComparison.OrdinalIgnoreCase),
                "Fons diagnostici realis falsus est.");
            File.WriteAllText(ViaRelationis, "RECTE: diagnosticum reale compilatoris per Officinam lectum est.\n");
            return 0;
        }
        catch (Exception erratum)
        {
            File.WriteAllText(ViaRelationis, erratum.ToString());
            return 1;
        }
        finally
        {
            if (Directory.Exists(radix))
            {
                Directory.Delete(radix, true);
            }
        }
    }

    public static async Task<int> ProbaNovumProiectumAsync(string compilator)
    {
        string radix = Path.Combine(Path.GetTempPath(), "officina-vindex-novum-" + Guid.NewGuid().ToString("N"));
        try
        {
            ProiectumVindex proiectum = FabricaProiectiVindex.Crea(radix);
            Exige(File.Exists(proiectum.ViaManifesti), "Manifestum novi proiecti deest.");
            Exige(File.Exists(proiectum.ViaFontis), "Fons novi proiecti deest.");
            Exige(proiectum.Destinatio == "PE", "Destinatio novi proiecti non est PE.");

            bool rescriptioRecusata = false;
            try
            {
                _ = FabricaProiectiVindex.Crea(radix);
            }
            catch (InvalidOperationException)
            {
                rescriptioRecusata = true;
            }
            Exige(rescriptioRecusata, "Fabrica proiectum exsistens rescribere permisit.");

            ResultatumProcessus compilatio = await ExecutorVindex.ConstrueAsync(compilator, proiectum);
            Exige(compilatio.Status == 0, compilatio.Exitus + compilatio.Errata);
            Exige(File.Exists(proiectum.ViaProducti), "Productum novi proiecti deest.");
            ResultatumProcessus executio = await ExecutorVindex.ExsequereAsync(proiectum);
            Exige(executio.Status == 0, executio.Exitus + executio.Errata);
            Exige(executio.Exitus.Replace("\r\n", "\n").Trim() == "Salve, VINDEX!", "Exitus novi proiecti differt.");
            File.WriteAllText(ViaRelationis, "RECTE: novum proiectum creatum, constructum et exsecutum est.\n");
            return 0;
        }
        catch (Exception erratum)
        {
            File.WriteAllText(ViaRelationis, erratum.ToString());
            return 1;
        }
        finally
        {
            if (Directory.Exists(radix))
            {
                Directory.Delete(radix, true);
            }
        }
    }

    private static void Exige(bool conditio, string nuntius)
    {
        if (!conditio)
        {
            throw new InvalidOperationException(nuntius);
        }
    }
}
