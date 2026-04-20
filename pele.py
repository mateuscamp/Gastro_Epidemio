from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def menu():
    opcoes = "[1] Ver Cadastrados\n[2] Novo Cadastro\n[3] Editar Cadastro\n[4] Excluir Cadastro\n[5] Sair"
    console.print(
        Panel(
            opcoes,
            title="[bold blue]MENU PRINCIPAL[/bold blue]",
            expand=False,
            subtitle="Escolha uma opção",
        )
    )
    console.print()


def submenu(titulo, subtitulo=None):
    opcoes = "[1] SIM\n[2] NÃO"
    console.print(
        Panel(
            opcoes,
            title=f"[bold red]{titulo}[/bold red]",
            subtitle=f"[yellow]{subtitulo}[/yellow]",
        )
    )
    console.print()


def listar(dados):
    tabela = Table(title="Pessoas Cadastradas")

    tabela.add_column("Nome", style="cyan", no_wrap=True)
    tabela.add_column("Idade", style="magenta", justify="right")

    for nome, idade in dados:
        tabela.add_row(nome, f"{idade} anos")

    console.print(tabela)


def cabeçalho(txt):
    console.print(Panel(f"[cyan]{txt}[/cyan]", expand=False))


def msg_erro(txt):
    console.print(Panel(f"[red]ERRO:[/red] {txt}"))


def msg_sucesso(txt):
    console.print(Panel(f"[green]Sucesso:[/green] {txt}", expand=False))


def msg_aviso(txt):
    console.print(Panel(f"[yellow]Atenção![/yellow] {txt}"))
