import { useToast } from '@chakra-ui/react'

export const useErrorToast = () => {
  const toast = useToast()

  const showErrorToast = (title: string, description: string) => {
    toast({
      title,
      description,
      status: 'error',
      duration: 5000,
      isClosable: true,
    })
  }

  return { showErrorToast }
}