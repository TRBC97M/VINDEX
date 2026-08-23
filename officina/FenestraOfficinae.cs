using System.ComponentModel;
using System.Drawing;
using System.Runtime.InteropServices;
using System.Text;
using System.Windows.Forms;

namespace Vindex.Officina;

internal sealed class FenestraOfficinae : Form
{
    private readonly ConfiguratioOfficinae _configuratio;
    private readonly string? _manifestumInitiale;
    private readonly Dictionary<string, DocumentumApertum> _documenta = new(StringComparer.OrdinalIgnoreCase);

    private readonly TreeView _arbor = new();
    private readonly TabControl _tabulaEditorum = new();
    private readonly TabControl _tabulaInferior = new();
    private readonly RichTextBox _exitus = new();
    private readonly ListView _diagnostica = new();
    private readonly Label _viaProiecti = new();
    private readonly Label _statusActus = new();
    private readonly Label _statusLoci = new();
    private readonly Label _statusDestinationis = new();
    private readonly Button _bullaConstructionis;
    private readonly Button _bullaExecutionis;

    private ProiectumVindex? _proiectum;
    private bool _colorans;

    public FenestraOfficinae(ConfiguratioOfficinae configuratio, string? manifestumInitiale)
    {
        _configuratio = configuratio;
        _manifestumInitiale = manifestumInitiale;
        Text = configuratio.Titulus;
        Width = configuratio.Latitudo;
        Height = configuratio.Altitudo;
        MinimumSize = new Size(1024, 680);
        StartPosition = FormStartPosition.CenterScreen;
        BackColor = Color("COLOR_FUNDUM", "#070C13");
        ForeColor = Color("COLOR_TEXTUS", "#D9E6F2");
        Font = new Font("Segoe UI", 9.5f);
        AutoScaleMode = AutoScaleMode.Dpi;
        KeyPreview = true;

        TableLayoutPanel radix = new()
        {
            Dock = DockStyle.Fill,
            ColumnCount = 1,
            RowCount = 4,
            BackColor = BackColor,
            Padding = Padding.Empty,
        };
        radix.RowStyles.Add(new RowStyle(SizeType.Absolute, 58));
        radix.RowStyles.Add(new RowStyle(SizeType.Absolute, 54));
        radix.RowStyles.Add(new RowStyle(SizeType.Percent, 100));
        radix.RowStyles.Add(new RowStyle(SizeType.Absolute, 29));
        Controls.Add(radix);

        radix.Controls.Add(CreaCaput(), 0, 0);
        FlowLayoutPanel instrumenta = CreaInstrumenta();
        radix.Controls.Add(instrumenta, 0, 1);
        radix.Controls.Add(CreaCorpus(), 0, 2);
        radix.Controls.Add(CreaStatum(), 0, 3);

        _bullaConstructionis = (Button)instrumenta.Controls.Find("construe", false).Single();
        _bullaExecutionis = (Button)instrumenta.Controls.Find("exsequere", false).Single();

        Shown += (_, _) =>
        {
            AspectusWindows.Applica(Handle, Color("COLOR_FUNDUM", "#070C13"));
            if (!string.IsNullOrWhiteSpace(_manifestumInitiale))
            {
                AperiProiectum(_manifestumInitiale);
            }
            else
            {
                ScribeExitum("VINDEX Officina — Gradus A\nAperi manifestum proiecti ut incipias.\n");
            }
        };
        FormClosing += FenestraClauditur;
        KeyDown += ClavisPressa;
    }

    private Panel CreaCaput()
    {
        Panel caput = new()
        {
            Dock = DockStyle.Fill,
            BackColor = Color("COLOR_SUPERFICIEI", "#0D1621"),
            Padding = new Padding(18, 8, 18, 7),
        };
        Panel linea = new()
        {
            Dock = DockStyle.Bottom,
            Height = 1,
            BackColor = Color("COLOR_LIMINIS", "#28445C"),
        };
        Label marca = new()
        {
            AutoSize = true,
            Text = _configuratio.Titulus,
            ForeColor = Color("COLOR_ACCENTUS", "#65C8FF"),
            Font = new Font("Segoe UI Semibold", 15f, FontStyle.Bold),
            Location = new Point(18, 8),
        };
        Label subtitulus = new()
        {
            AutoSize = true,
            Text = _configuratio.Subtitulus,
            ForeColor = Color("COLOR_TEXTUS_OBSCURI", "#8096A8"),
            Font = new Font("Segoe UI", 8f, FontStyle.Bold),
            Location = new Point(20, 36),
        };
        _viaProiecti.AutoEllipsis = true;
        _viaProiecti.TextAlign = ContentAlignment.MiddleRight;
        _viaProiecti.Text = "NULLUM PROIECTUM";
        _viaProiecti.ForeColor = Color("COLOR_TEXTUS_OBSCURI", "#8096A8");
        _viaProiecti.Dock = DockStyle.Right;
        _viaProiecti.Width = 600;
        caput.Controls.Add(_viaProiecti);
        caput.Controls.Add(marca);
        caput.Controls.Add(subtitulus);
        caput.Controls.Add(linea);
        return caput;
    }

    private FlowLayoutPanel CreaInstrumenta()
    {
        FlowLayoutPanel instrumenta = new()
        {
            Dock = DockStyle.Fill,
            BackColor = Color("COLOR_SUPERFICIEI", "#0D1621"),
            FlowDirection = FlowDirection.LeftToRight,
            WrapContents = false,
            Padding = new Padding(13, 8, 8, 7),
        };

        Button aperi = CreaBullam("aperi", _configuratio.Valor("ACTIO_APERI", "APERI PROIECTUM"), Color("COLOR_ACCENTUS", "#65C8FF"));
        aperi.Click += (_, _) => AperiProiectumDialogo();
        Button serva = CreaBullam("serva", _configuratio.Valor("ACTIO_SERVA", "SERVA"), Color("COLOR_TEXTUS", "#D9E6F2"));
        serva.Click += (_, _) => ServaOmnia();
        Button construe = CreaBullam("construe", _configuratio.Valor("ACTIO_CONSTRUE", "CONSTRUE"), Color("COLOR_ACCENTUS_SECUNDI", "#B38CFF"));
        construe.Click += async (_, _) => await ConstrueAsync(false);
        Button exsequere = CreaBullam("exsequere", _configuratio.Valor("ACTIO_EXSEQUERE", "EXSEQUERE"), Color("COLOR_RECTI", "#70D99A"));
        exsequere.Click += async (_, _) => await ConstrueAsync(true);

        instrumenta.Controls.Add(aperi);
        instrumenta.Controls.Add(serva);
        instrumenta.Controls.Add(CreaSeparatorem());
        instrumenta.Controls.Add(construe);
        instrumenta.Controls.Add(exsequere);
        return instrumenta;
    }

    private Control CreaCorpus()
    {
        SplitContainer corpus = new()
        {
            Dock = DockStyle.Fill,
            Orientation = Orientation.Vertical,
            SplitterDistance = 270,
            SplitterWidth = 5,
            BackColor = Color("COLOR_LIMINIS", "#28445C"),
            Panel1MinSize = 190,
            Panel2MinSize = 500,
        };
        corpus.Panel1.BackColor = Color("COLOR_SUPERFICIEI", "#0D1621");
        corpus.Panel2.BackColor = Color("COLOR_EDITORIS", "#050910");
        corpus.Panel1.Controls.Add(CreaExploratorem());
        corpus.Panel2.Controls.Add(CreaEditorEtExitum());
        return corpus;
    }

    private Control CreaExploratorem()
    {
        Panel pannus = new()
        {
            Dock = DockStyle.Fill,
            BackColor = Color("COLOR_SUPERFICIEI", "#0D1621"),
            Padding = new Padding(10, 9, 8, 8),
        };
        Label titulus = new()
        {
            Dock = DockStyle.Top,
            Height = 31,
            Text = _configuratio.Valor("NOMEN_PROIECTI", "PROIECTUM"),
            ForeColor = Color("COLOR_TEXTUS_OBSCURI", "#8096A8"),
            Font = new Font("Segoe UI", 8.5f, FontStyle.Bold),
            TextAlign = ContentAlignment.MiddleLeft,
            Padding = new Padding(5, 0, 0, 0),
        };
        _arbor.Dock = DockStyle.Fill;
        _arbor.BorderStyle = BorderStyle.None;
        _arbor.BackColor = Color("COLOR_SUPERFICIEI", "#0D1621");
        _arbor.ForeColor = Color("COLOR_TEXTUS", "#D9E6F2");
        _arbor.Font = new Font("Segoe UI", 9.5f);
        _arbor.HideSelection = false;
        _arbor.FullRowSelect = true;
        _arbor.ShowLines = false;
        _arbor.NodeMouseDoubleClick += (_, eventum) =>
        {
            if (eventum.Node.Tag is string via && File.Exists(via) && EstTextuale(via))
            {
                AperiDocumentum(via);
            }
        };
        pannus.Controls.Add(_arbor);
        pannus.Controls.Add(titulus);
        return pannus;
    }

    private Control CreaEditorEtExitum()
    {
        SplitContainer divisio = new()
        {
            Dock = DockStyle.Fill,
            Orientation = Orientation.Horizontal,
            SplitterDistance = 535,
            SplitterWidth = 5,
            BackColor = Color("COLOR_LIMINIS", "#28445C"),
            Panel1MinSize = 250,
            Panel2MinSize = 145,
        };
        PraeparaTabulam(_tabulaEditorum);
        PraeparaTabulam(_tabulaInferior);
        _tabulaEditorum.Dock = DockStyle.Fill;
        _tabulaInferior.Dock = DockStyle.Fill;
        divisio.Panel1.Controls.Add(_tabulaEditorum);

        _exitus.Dock = DockStyle.Fill;
        _exitus.ReadOnly = true;
        _exitus.BorderStyle = BorderStyle.None;
        _exitus.BackColor = Color("COLOR_EDITORIS", "#050910");
        _exitus.ForeColor = Color("COLOR_TEXTUS", "#D9E6F2");
        _exitus.Font = new Font("Cascadia Mono", 10f);
        _exitus.WordWrap = false;
        TabPage tabExitus = CreaTabulam(_configuratio.Valor("NOMEN_EXITUS", "EXITUS"));
        tabExitus.Controls.Add(_exitus);

        _diagnostica.Dock = DockStyle.Fill;
        _diagnostica.View = View.Details;
        _diagnostica.FullRowSelect = true;
        _diagnostica.GridLines = false;
        _diagnostica.BorderStyle = BorderStyle.None;
        _diagnostica.BackColor = Color("COLOR_EDITORIS", "#050910");
        _diagnostica.ForeColor = Color("COLOR_TEXTUS", "#D9E6F2");
        _diagnostica.Font = new Font("Segoe UI", 9f);
        _diagnostica.Columns.Add("FONS", 260);
        _diagnostica.Columns.Add("LINEA", 75);
        _diagnostica.Columns.Add("COLUMNA", 85);
        _diagnostica.Columns.Add("NUNTIUS", 650);
        _diagnostica.DoubleClick += (_, _) => NavigaAdDiagnosticum();
        TabPage tabDiagnostica = CreaTabulam(_configuratio.Valor("NOMEN_DIAGNOSTICORUM", "DIAGNOSTICA"));
        tabDiagnostica.Controls.Add(_diagnostica);

        _tabulaInferior.TabPages.Add(tabExitus);
        _tabulaInferior.TabPages.Add(tabDiagnostica);
        divisio.Panel2.Controls.Add(_tabulaInferior);
        return divisio;
    }

    private Control CreaStatum()
    {
        TableLayoutPanel status = new()
        {
            Dock = DockStyle.Fill,
            BackColor = Color("COLOR_SUPERFICIEI_ALTAE", "#132130"),
            ColumnCount = 3,
            Padding = new Padding(12, 0, 12, 0),
        };
        status.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100));
        status.ColumnStyles.Add(new ColumnStyle(SizeType.Absolute, 150));
        status.ColumnStyles.Add(new ColumnStyle(SizeType.Absolute, 120));
        PraeparaStatum(_statusActus, ContentAlignment.MiddleLeft, "PARATA");
        PraeparaStatum(_statusLoci, ContentAlignment.MiddleCenter, "LINEA 1 : 1");
        PraeparaStatum(_statusDestinationis, ContentAlignment.MiddleRight, "—");
        status.Controls.Add(_statusActus, 0, 0);
        status.Controls.Add(_statusLoci, 1, 0);
        status.Controls.Add(_statusDestinationis, 2, 0);
        return status;
    }

    private Button CreaBullam(string nomen, string textus, Color accentus)
    {
        Button bulla = new()
        {
            Name = nomen,
            Text = textus,
            AutoSize = true,
            Height = 35,
            FlatStyle = FlatStyle.Flat,
            BackColor = Color("COLOR_SUPERFICIEI_ALTAE", "#132130"),
            ForeColor = accentus,
            Font = new Font("Segoe UI", 9f, FontStyle.Bold),
            Cursor = Cursors.Hand,
            Margin = new Padding(4, 0, 4, 0),
            Padding = new Padding(10, 2, 10, 2),
        };
        bulla.FlatAppearance.BorderColor = Color("COLOR_LIMINIS", "#28445C");
        bulla.FlatAppearance.MouseOverBackColor = Color("COLOR_SUPERFICIEI_ALTAE", "#132130");
        bulla.FlatAppearance.MouseDownBackColor = Color("COLOR_FUNDUM", "#070C13");
        return bulla;
    }

    private Control CreaSeparatorem() => new Panel
    {
        Width = 1,
        Height = 31,
        BackColor = Color("COLOR_LIMINIS", "#28445C"),
        Margin = new Padding(9, 2, 9, 0),
    };

    private TabPage CreaTabulam(string titulus) => new(titulus)
    {
        BackColor = Color("COLOR_EDITORIS", "#050910"),
        ForeColor = Color("COLOR_TEXTUS", "#D9E6F2"),
        Padding = new Padding(0),
    };

    private void PraeparaTabulam(TabControl tabula)
    {
        tabula.DrawMode = TabDrawMode.OwnerDrawFixed;
        tabula.ItemSize = new Size(160, 28);
        tabula.SizeMode = TabSizeMode.Fixed;
        tabula.Padding = new Point(12, 4);
        tabula.DrawItem += (_, eventum) =>
        {
            bool electa = eventum.Index == tabula.SelectedIndex;
            Color fundum = electa
                ? Color("COLOR_SUPERFICIEI_ALTAE", "#132130")
                : Color("COLOR_SUPERFICIEI", "#0D1621");
            using SolidBrush peniculus = new(fundum);
            eventum.Graphics.FillRectangle(peniculus, eventum.Bounds);
            TextRenderer.DrawText(
                eventum.Graphics,
                tabula.TabPages[eventum.Index].Text,
                new Font("Segoe UI", 8.5f, electa ? FontStyle.Bold : FontStyle.Regular),
                eventum.Bounds,
                electa ? Color("COLOR_ACCENTUS", "#65C8FF") : Color("COLOR_TEXTUS_OBSCURI", "#8096A8"),
                TextFormatFlags.HorizontalCenter | TextFormatFlags.VerticalCenter | TextFormatFlags.EndEllipsis);
        };
    }

    private void PraeparaStatum(Label label, ContentAlignment alignatio, string textus)
    {
        label.Dock = DockStyle.Fill;
        label.TextAlign = alignatio;
        label.Text = textus;
        label.ForeColor = Color("COLOR_TEXTUS_OBSCURI", "#8096A8");
        label.Font = new Font("Segoe UI", 8.5f, FontStyle.Bold);
    }

    private void AperiProiectumDialogo()
    {
        using OpenFileDialog dialogus = new()
        {
            Title = "Manifestum proiecti VINDEX aperi",
            Filter = "Proiectum VINDEX|proiectum*.vindex|Fontes VINDEX|*.vindex|Omnia|*.*",
            CheckFileExists = true,
            Multiselect = false,
        };
        if (dialogus.ShowDialog(this) == DialogResult.OK)
        {
            AperiProiectum(dialogus.FileName);
        }
    }

    private void AperiProiectum(string viaManifesti)
    {
        if (!LicetMutareProiectum())
        {
            return;
        }

        try
        {
            ProiectumVindex novum = ProiectumVindex.Lege(viaManifesti);
            ClaudeDocumenta();
            _proiectum = novum;
            _viaProiecti.Text = novum.ViaManifesti;
            _statusDestinationis.Text = novum.Destinatio;
            RecreaArborem();
            AperiDocumentum(novum.ViaFontis);
            _diagnostica.Items.Clear();
            _exitus.Clear();
            ScribeExitum($"RECTE: proiectum apertum est.\nFONS: {novum.ViaFontis}\nPRODUCTUM: {novum.ViaProducti}\nDESTINATIO: {novum.Destinatio}\n");
            StatueActum("PROIECTUM PARATUM", true);
        }
        catch (Exception erratum)
        {
            MessageBox.Show(this, erratum.Message, "ERRATUM PROIECTI", MessageBoxButtons.OK, MessageBoxIcon.Error);
            StatueActum("ERRATUM PROIECTI", false);
        }
    }

    private void RecreaArborem()
    {
        _arbor.BeginUpdate();
        try
        {
            _arbor.Nodes.Clear();
            if (_proiectum is null)
            {
                return;
            }
            TreeNode radix = new(Path.GetFileName(_proiectum.Radix)) { Tag = _proiectum.Radix };
            AddeDirectorium(radix, _proiectum.Radix);
            _arbor.Nodes.Add(radix);
            radix.Expand();
        }
        finally
        {
            _arbor.EndUpdate();
        }
    }

    private void AddeDirectorium(TreeNode parens, string directorium)
    {
        IEnumerable<string> directoria = Directory.EnumerateDirectories(directorium)
            .Where(via => !EstDirectoriumInternum(via))
            .OrderBy(via => via, StringComparer.OrdinalIgnoreCase);
        foreach (string via in directoria)
        {
            TreeNode nodus = new(Path.GetFileName(via)) { Tag = via };
            AddeDirectorium(nodus, via);
            parens.Nodes.Add(nodus);
        }
        foreach (string via in Directory.EnumerateFiles(directorium).OrderBy(via => via, StringComparer.OrdinalIgnoreCase))
        {
            parens.Nodes.Add(new TreeNode(Path.GetFileName(via)) { Tag = via });
        }
    }

    private static bool EstDirectoriumInternum(string via)
    {
        string nomen = Path.GetFileName(via);
        return nomen.Equals(".git", StringComparison.OrdinalIgnoreCase)
            || nomen.Equals("bin", StringComparison.OrdinalIgnoreCase)
            || nomen.Equals("obj", StringComparison.OrdinalIgnoreCase)
            || nomen.Equals("distributio", StringComparison.OrdinalIgnoreCase);
    }

    private static bool EstTextuale(string via)
    {
        string extensio = Path.GetExtension(via);
        return extensio.Equals(".vindex", StringComparison.OrdinalIgnoreCase)
            || extensio.Equals(".forma", StringComparison.OrdinalIgnoreCase)
            || extensio.Equals(".stilus", StringComparison.OrdinalIgnoreCase)
            || extensio.Equals(".md", StringComparison.OrdinalIgnoreCase)
            || extensio.Equals(".txt", StringComparison.OrdinalIgnoreCase);
    }

    private void AperiDocumentum(string via)
    {
        string plena = Path.GetFullPath(via);
        if (_documenta.TryGetValue(plena, out DocumentumApertum? apertum))
        {
            _tabulaEditorum.SelectedTab = apertum.Tabula;
            apertum.Editor.Focus();
            return;
        }
        if (!File.Exists(plena))
        {
            MessageBox.Show(this, "Fasciculus non inventus est.", "ERRATUM", MessageBoxButtons.OK, MessageBoxIcon.Error);
            return;
        }

        RichTextBox editor = new()
        {
            Dock = DockStyle.Fill,
            BorderStyle = BorderStyle.None,
            BackColor = Color("COLOR_EDITORIS", "#050910"),
            ForeColor = Color("COLOR_TEXTUS", "#D9E6F2"),
            Font = new Font("Cascadia Code", 11f),
            AcceptsTab = true,
            DetectUrls = false,
            WordWrap = false,
            HideSelection = false,
            Text = File.ReadAllText(plena),
        };
        editor.SelectionTabs = Enumerable.Range(1, 64).Select(index => index * 32).ToArray();
        TabPage tabula = CreaTabulam(Path.GetFileName(plena));
        tabula.ToolTipText = plena;
        tabula.Controls.Add(editor);
        System.Windows.Forms.Timer mora = new() { Interval = 220 };
        DocumentumApertum documentum = new(plena, tabula, editor, mora);
        _documenta[plena] = documentum;
        _tabulaEditorum.TabPages.Add(tabula);
        _tabulaEditorum.SelectedTab = tabula;

        mora.Tick += (_, _) =>
        {
            mora.Stop();
            ColoraDocumentum(documentum);
        };
        editor.TextChanged += (_, _) =>
        {
            if (_colorans || !documentum.Paratum)
            {
                return;
            }
            documentum.Mutatum = true;
            RenovaTitulum(documentum);
            mora.Stop();
            mora.Start();
        };
        editor.SelectionChanged += (_, _) => RenovaLocum(editor);
        ColoraDocumentum(documentum);
        documentum.Paratum = true;
        editor.Modified = false;
        editor.Focus();
        RenovaLocum(editor);
    }

    private void ColoraDocumentum(DocumentumApertum documentum)
    {
        if (!documentum.Via.EndsWith(".vindex", StringComparison.OrdinalIgnoreCase))
        {
            return;
        }
        _colorans = true;
        try
        {
            ColoratorVindex.Colora(documentum.Editor, _configuratio);
        }
        finally
        {
            _colorans = false;
        }
    }

    private bool ServaOmnia()
    {
        try
        {
            foreach (DocumentumApertum documentum in _documenta.Values.Where(documentum => documentum.Mutatum))
            {
                File.WriteAllText(documentum.Via, documentum.Editor.Text, new UTF8Encoding(false));
                documentum.Mutatum = false;
                documentum.Editor.Modified = false;
                RenovaTitulum(documentum);
            }
            StatueActum("RECTE: FONTES SERVATI", true);
            return true;
        }
        catch (Exception erratum)
        {
            MessageBox.Show(this, erratum.Message, "ERRATUM SERVATIONIS", MessageBoxButtons.OK, MessageBoxIcon.Error);
            StatueActum("ERRATUM SERVATIONIS", false);
            return false;
        }
    }

    private async Task ConstrueAsync(bool exsequere)
    {
        if (_proiectum is null)
        {
            MessageBox.Show(this, "Primum proiectum VINDEX aperi.", "NULLUM PROIECTUM", MessageBoxButtons.OK, MessageBoxIcon.Information);
            return;
        }
        if (!ServaOmnia())
        {
            return;
        }
        string? compilator = InveniCompilatorem();
        if (compilator is null)
        {
            MessageBox.Show(this, "compilator_vindex.exe iuxta Officinam non inventus est.", "COMPILATOR DEEST", MessageBoxButtons.OK, MessageBoxIcon.Error);
            return;
        }

        ActivaAedificationem(false);
        _diagnostica.Items.Clear();
        _tabulaInferior.SelectedIndex = 0;
        ScribeExitum($"\n>>> CONSTRUE {Path.GetFileName(_proiectum.ViaManifesti)}\n");
        StatueActum("CONSTRUCTIO INCIPIT", true);
        try
        {
            ResultatumProcessus compilatio = await ExecutorVindex.ConstrueAsync(compilator, _proiectum);
            ScribeExitum(compilatio.Exitus);
            ScribeExitum(compilatio.Errata);
            ExhibeDiagnostica(compilatio.Exitus + "\n" + compilatio.Errata);
            if (compilatio.Status != 0)
            {
                ScribeExitum($"STATUS COMPILATIONIS: {compilatio.Status}\n");
                StatueActum("ERRATUM COMPILATIONIS", false);
                return;
            }

            ScribeExitum("RECTE: proiectum constructum est.\n");
            StatueActum("RECTE: CONSTRUCTUM", true);
            RecreaArborem();
            if (!exsequere)
            {
                return;
            }
            if (!File.Exists(_proiectum.ViaProducti))
            {
                throw new FileNotFoundException("Productum compilatum non inventum est.", _proiectum.ViaProducti);
            }

            ScribeExitum($"\n>>> EXSEQUERE {Path.GetFileName(_proiectum.ViaProducti)}\n");
            StatueActum("EXECUTIO INCIPIT", true);
            ResultatumProcessus executio = await ExecutorVindex.ExsequereAsync(_proiectum);
            ScribeExitum(executio.Exitus);
            ScribeExitum(executio.Errata);
            ScribeExitum($"STATUS EXECUTIONIS: {executio.Status}\n");
            StatueActum(executio.Status == 0 ? "RECTE: EXECUTUM" : "ERRATUM EXECUTIONIS", executio.Status == 0);
        }
        catch (Win32Exception erratum)
        {
            ScribeExitum($"ERRATUM: productum in hac destinatione exsequi non potest.\n{erratum.Message}\n");
            StatueActum("ERRATUM EXECUTIONIS", false);
        }
        catch (Exception erratum)
        {
            ScribeExitum($"ERRATUM: {erratum.Message}\n");
            StatueActum("ERRATUM", false);
        }
        finally
        {
            ActivaAedificationem(true);
        }
    }

    private string? InveniCompilatorem()
    {
        string? ambitus = Environment.GetEnvironmentVariable("VINDEX_COMPILATOR");
        IEnumerable<string?> candidati = new string?[]
        {
            ambitus,
            Path.Combine(AppContext.BaseDirectory, "compilator_vindex.exe"),
            Path.Combine(AppContext.BaseDirectory, "instrumenta", "compilator_vindex.exe"),
        };
        return candidati.FirstOrDefault(via => !string.IsNullOrWhiteSpace(via) && File.Exists(via));
    }

    private void ExhibeDiagnostica(string relatio)
    {
        IReadOnlyList<DiagnosticumVindex> inventa = DiagnosticumVindex.Extrahe(relatio);
        foreach (DiagnosticumVindex diagnosticum in inventa)
        {
            string nomen = Path.GetFileName(diagnosticum.Via);
            ListViewItem item = new(new[] { nomen, diagnosticum.Linea.ToString(), diagnosticum.Columna.ToString(), diagnosticum.Nuntius })
            {
                Tag = diagnosticum,
                ForeColor = Color("COLOR_ERRATI", "#FF7F91"),
            };
            _diagnostica.Items.Add(item);
        }
        if (inventa.Count > 0)
        {
            _tabulaInferior.SelectedIndex = 1;
        }
    }

    private void NavigaAdDiagnosticum()
    {
        if (_diagnostica.SelectedItems.Count == 0 || _diagnostica.SelectedItems[0].Tag is not DiagnosticumVindex diagnosticum || _proiectum is null)
        {
            return;
        }
        string via = Path.IsPathRooted(diagnosticum.Via)
            ? diagnosticum.Via
            : Path.GetFullPath(Path.Combine(_proiectum.Radix, diagnosticum.Via));
        if (!File.Exists(via))
        {
            return;
        }
        AperiDocumentum(via);
        DocumentumApertum documentum = _documenta[Path.GetFullPath(via)];
        int linea = Math.Max(0, diagnosticum.Linea - 1);
        int initium = documentum.Editor.GetFirstCharIndexFromLine(linea);
        if (initium < 0)
        {
            return;
        }
        int positio = Math.Min(documentum.Editor.TextLength, initium + Math.Max(0, diagnosticum.Columna - 1));
        documentum.Editor.Select(positio, 0);
        documentum.Editor.ScrollToCaret();
        documentum.Editor.Focus();
    }

    private void ScribeExitum(string textus)
    {
        if (string.IsNullOrEmpty(textus))
        {
            return;
        }
        _exitus.AppendText(textus.Replace("\r\n", "\n"));
        _exitus.SelectionStart = _exitus.TextLength;
        _exitus.ScrollToCaret();
    }

    private void RenovaTitulum(DocumentumApertum documentum)
        => documentum.Tabula.Text = (documentum.Mutatum ? "● " : string.Empty) + Path.GetFileName(documentum.Via);

    private void RenovaLocum(RichTextBox editor)
    {
        int linea = editor.GetLineFromCharIndex(editor.SelectionStart);
        int initium = editor.GetFirstCharIndexFromLine(linea);
        int columna = editor.SelectionStart - Math.Max(0, initium);
        _statusLoci.Text = $"LINEA {linea + 1} : {columna + 1}";
    }

    private void StatueActum(string textus, bool recte)
    {
        _statusActus.Text = textus;
        _statusActus.ForeColor = recte ? Color("COLOR_RECTI", "#70D99A") : Color("COLOR_ERRATI", "#FF7F91");
    }

    private void ActivaAedificationem(bool activa)
    {
        _bullaConstructionis.Enabled = activa;
        _bullaExecutionis.Enabled = activa;
        UseWaitCursor = !activa;
    }

    private bool LicetMutareProiectum()
    {
        if (!_documenta.Values.Any(documentum => documentum.Mutatum))
        {
            return true;
        }
        DialogResult responsum = MessageBox.Show(
            this,
            "Fontes mutati sunt. Vis eos servare?",
            "FONTES MUTATI",
            MessageBoxButtons.YesNoCancel,
            MessageBoxIcon.Question);
        if (responsum == DialogResult.Cancel)
        {
            return false;
        }
        return responsum != DialogResult.Yes || ServaOmnia();
    }

    private void ClaudeDocumenta()
    {
        foreach (DocumentumApertum documentum in _documenta.Values)
        {
            documentum.Mora.Dispose();
        }
        _documenta.Clear();
        _tabulaEditorum.TabPages.Clear();
    }

    private void FenestraClauditur(object? mittens, FormClosingEventArgs eventum)
    {
        if (!LicetMutareProiectum())
        {
            eventum.Cancel = true;
        }
    }

    private void ClavisPressa(object? mittens, KeyEventArgs eventum)
    {
        if (eventum.Control && eventum.KeyCode == Keys.O)
        {
            AperiProiectumDialogo();
            eventum.SuppressKeyPress = true;
        }
        else if (eventum.Control && eventum.KeyCode == Keys.S)
        {
            ServaOmnia();
            eventum.SuppressKeyPress = true;
        }
        else if (eventum.KeyCode == Keys.F7)
        {
            _ = ConstrueAsync(false);
            eventum.SuppressKeyPress = true;
        }
        else if (eventum.KeyCode == Keys.F5)
        {
            _ = ConstrueAsync(true);
            eventum.SuppressKeyPress = true;
        }
    }

    private Color Color(string nomen, string praedefinitus) => _configuratio.Color(nomen, praedefinitus);
}

internal sealed class DocumentumApertum(
    string via,
    TabPage tabula,
    RichTextBox editor,
    System.Windows.Forms.Timer mora)
{
    public string Via { get; } = via;
    public TabPage Tabula { get; } = tabula;
    public RichTextBox Editor { get; } = editor;
    public System.Windows.Forms.Timer Mora { get; } = mora;
    public bool Mutatum { get; set; }
    public bool Paratum { get; set; }
}

internal static class AspectusWindows
{
    [DllImport("dwmapi.dll")]
    private static extern int DwmSetWindowAttribute(IntPtr fenestra, int attributum, ref int valor, int magnitudo);

    public static void Applica(IntPtr fenestra, Color fundum)
    {
        try
        {
            int obscurum = 1;
            _ = DwmSetWindowAttribute(fenestra, 20, ref obscurum, sizeof(int));
            int color = fundum.R | (fundum.G << 8) | (fundum.B << 16);
            _ = DwmSetWindowAttribute(fenestra, 35, ref color, sizeof(int));
        }
        catch
        {
            // Aspectus systematis prior manet si DWM hoc attributum ignorat.
        }
    }
}
