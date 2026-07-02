// .vitepress/theme/index.ts
import DefaultTheme from 'vitepress/theme'
import { onMounted, watch, nextTick } from 'vue'
import { useRoute } from 'vitepress'

export default {
  extends: DefaultTheme,

  setup() {
    const route = useRoute()

    const runScript = async () => {
      await nextTick();
      // 此时DOM已渲染完成
      const MESSAGES = [
        "The river is moving. The blackbird must be flying.",
        "It was a small part of the pantomime.",
        "A man and a woman and a blackbird are one.",
        "It marked the edge of one of many circles.",
        "But I know, too, that the blackbird is involved in what I know."

      ];
      (document.querySelector(".message") as HTMLParagraphElement).innerText = MESSAGES[Math.floor(Math.random() * MESSAGES.length)];
    }

    onMounted(runScript)

    watch(
      () => route.path,
      () => {
        runScript()
      }
    )
  }
}