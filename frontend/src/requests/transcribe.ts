import { useMutation } from '@tanstack/react-query'
import axios from 'axios'
import { config } from '@/config'
import { useErrorToast } from '@/hooks/useErrorToast'

export const useTranscribeMutation = () => {
  const { showErrorToast } = useErrorToast()

  return useMutation({
    mutationFn: async (formData: FormData) => {
      const response = await axios.post(`${config.apiUrl}/transcribe`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      })
      return response.data.transcription
    },
    onError: () => {
      showErrorToast(
        'Transcription failed',
        'An error occurred during transcription. Please try again.'
      )
    }
  })
}