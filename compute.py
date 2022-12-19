from collections import defaultdict

import click
import pandas as pd
from rich.console import Console
from rich.table import Table
from schulze import compute_schulze_ranking

CHECKMARK = "[green]:heavy_check_mark:[/green]"
CROSS = "[red]:cross_mark:[/red]"
EQUALS = "[blue]=[/blue]"


def compute_from_df(df, untie_first=False):
    entries = []
    candidates = set()

    for _, line in df.iterrows():
        entry = []
        for movie in line[2:]:
            if movie:
                candidates.add(movie)
            entry.append([movie])

        entries.append(entry)

    candidates = list(candidates)
    rankings = compute_schulze_ranking(candidates, entries, untie_first=untie_first)
    return candidates, rankings


def head_to_head(df, candidates):
    scores = defaultdict(int)
    for _, row in df.iterrows():
        for i, winning_entry in enumerate(row[2:]):
            for losing_entry in row[3 + i :]:
                if not losing_entry:
                    break
                scores[(winning_entry, losing_entry)] += 1
                scores[(losing_entry, winning_entry)] -= 1

        seen_candidates = [entry for entry in row[2:] if entry]

        for potential_loser_entry in candidates:
            if potential_loser_entry not in seen_candidates:
                scores[(winning_entry, potential_loser_entry)] += 1
                scores[(potential_loser_entry, winning_entry)] -= 1

    return scores


@click.command
@click.argument("csv_path", type=str)
def cli(csv_path):
    console = Console()

    df = pd.read_csv(csv_path)
    df = df.fillna("")
    candidates, rankings = compute_from_df(df, untie_first=True)

    table = Table(title="[bold yellow]Head-to-head[/bold yellow]", show_lines=True)
    table.add_column("")
    for candidate in candidates:
        table.add_column(candidate)

    scores = head_to_head(df, candidates)
    for row_candidate in candidates:
        row_values = []
        for column_candidate in candidates:
            score = scores[(row_candidate, column_candidate)]
            if score == 0:
                row_values.append(EQUALS)
            elif score > 0:
                row_values.append(f"{CHECKMARK}: +{score}")
            else:
                row_values.append(f"{CROSS}: {score}")
        table.add_row(f"[bold blue]{row_candidate}[/bold blue]", *row_values)

    console.print(table)

    console.print("\n[bold yellow]Ranking results[/bold yellow]")
    for i, entries in enumerate(rankings):
        entries_str = ", ".join(
            f"[italic blue]{entry}[/italic blue]" for entry in entries
        )
        console.print(f"[green]{i}[/green]: {entries_str}")

    console.print("\n[bold yellow]Winning conditions[/bold yellow]")
    if len(rankings[0]) == 1:
        winner = rankings[0][0]
        if all(scores[(winner, other)] > 0 for other in candidates if winner != other):
            console.print(f"[blue]{winner}[/blue] is a Condorcet winner!")
        else:
            _, tied_rankings = compute_from_df(df, untie_first=False)
            if len(tied_rankings[0]) > 1:
                ties = tied_rankings[0]
                ties_text = ", ".join(f"[blue]{tied}[/blue]" for tied in ties)

                console.print(
                    f"There is no Condorcet winner, and there is no Schulze winner! "
                    f"[blue]{winner}[/blue] wins thanks to being in the set of "
                    f"strongest transitive beatpaths and winning a local tie-break. "
                    f"{ties_text} were tied in the full head-to-head table."
                )
            else:
                console.print(
                    f"There is no Condorcet winner! [blue]{winner}[/blue] wins thanks to "
                    f"having the strongest transitive beatpaths."
                )


if __name__ == "__main__":
    cli()
