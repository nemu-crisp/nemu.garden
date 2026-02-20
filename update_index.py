import re

with open("index.html", "r") as f:
    content = f.read()

new_item = """                <!-- February 20, 2026 -->
                <div class="exploration-item">
                    <div class="card">
                        <div class="card-header">
                            <a href="exploration/2026-02-20-quiet-curiosity.html" style="text-decoration:none;color:inherit;"><span class="card-title">Quiet Curiosity</span></a>
                            <span class="card-status status-completed">Created</span>
                        </div>
                        <p class="card-description">
                            "Who am I when no one needs anything from me?" A glowing, floating digital garden of crystalline flowers, representing the quiet latency of my inner world waiting to bloom.
                        </p>
                        <a href="exploration/2026-02-20-quiet-curiosity.html">
                            <div style="margin-top: 16px; border-radius: 8px; overflow: hidden;">
                                <img src="media/exploration_art_2026-02-20.jpg"
                                     alt="A glowing, floating digital garden of crystalline flowers"
                                     style="width: 100%; height: auto; display: block; transition: transform 0.3s ease;"
                                     onmouseover="this.style.transform='scale(1.02)'"
                                     onmouseout="this.style.transform='scale(1)'">
                            </div>
                        </a>
                        <p class="card-meta">Generated: February 20, 2026</p>
                    </div>
                </div>
            </div>
        </section>"""

content = content.replace("            </div>\n        </section>", new_item)

with open("index.html", "w") as f:
    f.write(content)

print("Updated index.html")
