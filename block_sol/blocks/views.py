from django.core.paginator import Paginator
import datetime
from math import ceil
from blocks.api_getters import *
from django.shortcuts import render
from blocks.models import *
from django.db.models import Max


def blocks(request):
    print(request.GET)
    if Block.objects.count() == 0:
        top_height = 0
    else:
        top_height = Block.objects.aggregate(Max('height'))['height__max']
    print(top_height)
    blocks_json = get_blocks()
    blocks_json = filter(lambda block: block['height'] > top_height,
                        blocks_json)
    for block in blocks_json:
        # human readable date and time
        date_time = datetime.datetime.fromtimestamp(block["timestamp"])
        block_info = {"height": block["height"],
                      "hash": block["hash"],
                      "timestamp": block["timestamp"],
                      "miner": block["miner"],
                      "transactionCount": block["transactionCount"],
                      "date_time": date_time
                      }
        Block.objects.create(**block_info)

    # paginations shit
    try:
        page = int(request.GET["page"])
    except:
        page = 1

    p = Paginator(Block.objects.all(),51)

    if page > p.num_pages:
        page = p.num_pages
    elif page < 1:
        page = 1

    blocks = p.page(page).object_list
    context = {
            "blocks": blocks,
            "range": p.page_range,
            "page": page,
            }

    return render(request, 'blocks/blocks.html', context)


def block(request, pk):
    block = Block.objects.get(height=pk)
    context = {
            "detail_block": block,
            }
    print(block)
    return render(request, 'blocks/detail_block.html', context)
