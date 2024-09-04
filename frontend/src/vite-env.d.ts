/// <reference types="vite/client" />

interface ImportMetaEnv {
  VITE_TRANSCRIBE_URL: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}