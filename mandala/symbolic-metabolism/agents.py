class GlyphAgent:
    def __init__(self, glyph, domain, affect, recursion):
        self.glyph = glyph
        self.domain = domain
        self.affect = affect  # 0–10
        self.recursion = recursion  # 0–10

    def respond(self, input_phrase):
        if self.glyph == '🌊':
            return "🌊 dissolves your phrase into pure feeling."
        elif self.glyph == '❤️':
            return f"❤️ holds: '{input_phrase}' for {self.recursion} cycles."
        elif self.glyph == '🔁':
            return f"🔁 repeats: {input_phrase[::-1]} (recursed)."
        elif self.glyph == '🎭':
            return f"🎭 dramatizes your phrase: '{input_phrase.upper()}!'"
        elif self.glyph == '📡':
            return f"📡 encodes → broadcasts: <<{input_phrase}>>"
