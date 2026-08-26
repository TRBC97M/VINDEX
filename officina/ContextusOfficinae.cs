using System.Drawing;
using System.Windows.Forms;

namespace Vindex.Officina;

internal sealed class ContextusOfficinae : ApplicationContext
{
    private readonly ConfiguratioOfficinae _configuratio;
    private int _numerusFenestrarum;

    public ContextusOfficinae(ConfiguratioOfficinae configuratio, string? manifestumInitiale)
    {
        _configuratio = configuratio;
        AperiFenestra(manifestumInitiale);
    }

    private void AperiFenestra(string? manifestum)
    {
        FenestraOfficinae fenestra = new(_configuratio, manifestum);
        AmplificatioGradusB.Applica(fenestra, _configuratio, AperiFenestra);
        _numerusFenestrarum++;
        fenestra.FormClosed += (_, _) =>
        {
            _numerusFenestrarum--;
            if (_numerusFenestrarum == 0)
            {
                ExitThread();
            }
        };
        fenestra.Show();
    }
}

internal static class AmplificatioGradusB
{
    public static void Applica(
        FenestraOfficinae fenestra,
        ConfiguratioOfficinae configuratio,
        Action<string?> aperiFenestra)
    {
        Control? aperi = fenestra.Controls.Find("aperi", true).FirstOrDefault();
        if (aperi?.Parent is not FlowLayoutPanel instrumenta || instrumenta.Controls.Find("novum", false).Length != 0)
        {
            return;
        }

        Button novum = new()
        {
            Name = "novum",
            Text = configuratio.Valor("ACTIO_NOVUM", "NOVUM PROIECTUM"),
            AutoSize = true,
            Height = 35,
            FlatStyle = FlatStyle.Flat,
            BackColor = configuratio.Color("COLOR_SUPERFICIEI_ALTAE", "#132130"),
            ForeColor = configuratio.Color("COLOR_RECTI", "#70D99A"),
            Font = new Font("Segoe UI", 9f, FontStyle.Bold),
            Cursor = Cursors.Hand,
            Margin = new Padding(4, 0, 4, 0),
            Padding = new Padding(10, 2, 10, 2),
        };
        novum.FlatAppearance.BorderColor = configuratio.Color("COLOR_LIMINIS", "#28445C");
        novum.FlatAppearance.MouseOverBackColor = configuratio.Color("COLOR_SUPERFICIEI_ALTAE", "#132130");
        novum.FlatAppearance.MouseDownBackColor = configuratio.Color("COLOR_FUNDUM", "#070C13");
        novum.Click += (_, _) => CreaEtAperi(fenestra, aperiFenestra);
        instrumenta.Controls.Add(novum);
        instrumenta.Controls.SetChildIndex(novum, 0);

        fenestra.KeyDown += (_, eventum) =>
        {
            if (eventum.Control && eventum.KeyCode == Keys.N)
            {
                CreaEtAperi(fenestra, aperiFenestra);
                eventum.SuppressKeyPress = true;
            }
        };
    }

    private static void CreaEtAperi(FenestraOfficinae parens, Action<string?> aperiFenestra)
    {
        using FolderBrowserDialog dialogus = new()
        {
            Description = "Directorium novi proiecti VINDEX elige aut crea",
            ShowNewFolderButton = true,
            UseDescriptionForTitle = true,
        };
        if (dialogus.ShowDialog(parens) != DialogResult.OK)
        {
            return;
        }

        try
        {
            ProiectumVindex proiectum = FabricaProiectiVindex.Crea(dialogus.SelectedPath);
            aperiFenestra(proiectum.ViaManifesti);
        }
        catch (Exception erratum)
        {
            MessageBox.Show(parens, erratum.Message, "ERRATUM NOVI PROIECTI", MessageBoxButtons.OK, MessageBoxIcon.Error);
        }
    }
}
