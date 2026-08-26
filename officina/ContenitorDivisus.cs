global using SplitContainer = Vindex.Officina.ContenitorDivisus;

namespace Vindex.Officina;

// WinForms creat SplitContainer parvissimum antequam Dock layout applicetur.
// Gradus A autem minima tabularum statim in initializatore statuit; ideo
// continens initio mensuram realisticam accipit, deinde Dock eam ad fenestram
// veram accommodat. Sic regulae minimarum mensurarum iam in constructione valent.
internal sealed class ContenitorDivisus : System.Windows.Forms.SplitContainer
{
    public ContenitorDivisus()
    {
        Size = new System.Drawing.Size(1200, 800);
    }
}
