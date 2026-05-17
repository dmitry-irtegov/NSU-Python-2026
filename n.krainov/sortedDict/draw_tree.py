import sys
import random
from typing import Dict, List, Optional, Tuple

import matplotlib.pyplot as plt

from sortedDict import Color, K, SortedDict, SortedDictNode, T


def compute_positions(
    node: SortedDictNode[K, T],
    none_node: SortedDictNode[K, T],
    depth: int = 0,
    counter: Optional[List[int]] = None,
) -> Dict[int, Tuple[int, int, SortedDictNode[K, T]]]:
    if counter is None:
        counter = [0]
    positions: Dict[int, Tuple[int, int, SortedDictNode[K, T]]] = {}
    if node == none_node:
        return positions
    positions.update(compute_positions(node.leftChild, none_node, depth + 1, counter))
    positions[id(node)] = (counter[0], depth, node)
    counter[0] += 1
    positions.update(compute_positions(node.rightChild, none_node, depth + 1, counter))
    return positions


def draw_tree(d: SortedDict[K, T], title: str) -> None:
    positions: Dict[int, Tuple[int, int, SortedDictNode[K, T]]] = compute_positions(
        d._root, d._noneNode
    )

    nodes_by_id: Dict[int, SortedDictNode[K, T]] = {}
    counters: Dict[int, int] = {}
    for pos_id, (x, depth, node) in positions.items():
        nodes_by_id[pos_id] = node
        counters[pos_id] = node._counter

    fig, ax = plt.subplots(1, 1, figsize=(20, 12))
    ax.set_aspect('equal')
    ax.axis('off')

    rebalance_info: str = (
        f"Insert rebalances: {d._counterInsertRebalance}, "
        f"Delete rebalances: {d._counterDeleteRebalance}"
    )
    fig.suptitle(f'Red-Black Tree: {title}\n{rebalance_info}')

    node_radius: float = 1.6
    y_scale: float = 10

    for pos_id, (x, depth, node) in positions.items():
        y: float = -depth * y_scale
        for child in (node.leftChild, node.rightChild):
            if child != d._noneNode:
                child_id: int = id(child)
                cx: int
                cdepth: int
                cx, cdepth, _ = positions[child_id]
                cy: float = -cdepth * y_scale
                ax.plot([x, cx], [y, cy], color='#aaaaaa', linewidth=0.8, zorder=1)

    for pos_id, (x, depth, node) in positions.items():
        y = -depth * y_scale
        v: int = counters[pos_id]

        fill_color: str = '#e74c3c' if node.color == Color.RED else '#2c3e50'
        edge_color: str = '#c0392b' if node.color == Color.RED else '#1a1a1a'

        circle = plt.Circle((x, y), node_radius, color=fill_color, zorder=2)
        ax.add_patch(circle)
        ring = plt.Circle(
            (x, y), node_radius, fill=False,
            edgecolor=edge_color, linewidth=2.0, zorder=3,
        )
        ax.add_patch(ring)

        brightness: float = (
            0.299 * int(fill_color[1:3], 16) / 255 +
            0.587 * int(fill_color[3:5], 16) / 255 +
            0.114 * int(fill_color[5:7], 16) / 255
        )
        text_color: str = 'black' if brightness > 0.5 else 'white'
        ax.text(
            x, y + 0.48, str(node.key), ha='center', va='center',
            fontsize=6.5, color=text_color, fontweight='bold', zorder=4,
        )
        ax.text(
            x, y - 0.64, f'x{v}', ha='center', va='center',
            fontsize=5.5, color=text_color, zorder=4,
        )

    ax.plot([], [], color='#c0392b', linewidth=2, label='RED узел')
    ax.plot([], [], color='#1a1a1a', linewidth=2, label='BLACK узел')
    ax.legend(loc='upper right', fontsize=9)
    ax.autoscale()

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    mode: str = sys.argv[1] if len(sys.argv) > 1 else 'ascending'
    keys: List[int] = list(range(50))
    if mode == 'random':
        random.seed(42)
        random.shuffle(keys)
        title: str = 'random keys 0–50'
    else:
        title: str = 'ascending keys 0–50'

    d: SortedDict[int, str] = SortedDict[int, str]()
    for k in keys:
        d[k] = str(k)

    draw_tree(d, title)